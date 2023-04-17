import org.bytedeco.javacv.FFmpegFrameGrabber;
import org.bytedeco.javacv.Frame;
import org.bytedeco.javacv.FrameGrabber;
import org.bytedeco.javacv.Java2DFrameConverter;
import org.bytedeco.javacv.OpenCVFrameConverter;
import org.bytedeco.opencv.opencv_core.IplImage;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class FrameProcessor {
    public static void frameClipper(String[] args) {
        //open the input video file
        FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(args[0]);

        //get the frames per second (fps) of the input video
        double fps = 0;
        try {
            grabber.start();
            fps = grabber.getFrameRate();
        } catch (FrameGrabber.Exception e) {
            e.printStackTrace();
        }

        //compute the starting and the ending frame numbers
        double startTime = Double.parseDouble(args[1]);
        double endTime = Double.parseDouble(args[2]);
        int startFrame = (int) (startTime * fps);
        int endFrame = (int) (endTime * fps);

        //define the codec and get the output video file
        String codec = "mp4v";
        String outputVideo = args[3];

        //read the frames of the video and write them to the output video file
        try {
            grabber.setFrameNumber(startFrame);
            Frame frame = grabber.grab();
            OpenCVFrameConverter.ToIplImage converter = new OpenCVFrameConverter.ToIplImage();
            IplImage image = converter.convert(frame);
            int width = image.width();
            int height = image.height();
            FFmpegFrameGrabber grabber2 = new FFmpegFrameGrabber(outputVideo);
            grabber2.setImageWidth(width);
            grabber2.setImageHeight(height);
            grabber2.setVideoCodec(codec);
            grabber2.setFormat("mp4");
            grabber2.start();
            int i = 0;
            while (i < endFrame - startFrame) {
                grabber2.setTimestamp(grabber.getTimestamp());
                grabber2.record(frame);
                frame = grabber.grab();
                i++;
            }
            grabber2.stop();
            grabber2.release();
            grabber.stop();
            grabber.release();
        } catch (FrameGrabber.Exception e) {
            e.printStackTrace();
        }

        //release the resources
        grabber.stop();
        grabber.release();

    }


    //add a function to convert the video to aspect ratio 9:16

    public static void convertVideoToAspectRatio(String inputVideo, String outputVideo) {
        FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(inputVideo);
        try {
            grabber.start();
            int width = grabber.getImageWidth();
            int height = grabber.getImageHeight();
            int newWidth = 0;
            int newHeight = 0;
            if (width > height) {
                newWidth = height * 9 / 16;
                newHeight = height;
            } else {
                newWidth = width;
                newHeight = width * 16 / 9;
            }
            String command = "ffmpeg -i " + inputVideo + " -vf scale=" + newWidth + ":" + newHeight + " " + outputVideo;
            Process process = Runtime.getRuntime().exec(command);
            process.waitFor();
            grabber.stop();
            grabber.release();
        } catch (FrameGrabber.Exception | IOException | InterruptedException e) {
            e.printStackTrace();
        }

        //release the resources
        grabber.stop();
        grabber.release();
    }

    //add a function to get duration of the video

    public static double getVideoDuration(String inputVideo) {
        FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(inputVideo);
        double duration = 0;
        try {
            grabber.start();
            duration = grabber.getLengthInTime() / 1000000;
            grabber.stop();
            grabber.release();
        } catch (FrameGrabber.Exception e) {
            e.printStackTrace();
        }
    }

    //add a function to slice an audio file from the beginning to the given duration

    public static void sliceAudio(String inputAudio, String outputAudio, double duration) {
        String command = "ffmpeg -i " + inputAudio + " -t " + duration + " " + outputAudio;
        try {
            Process process = Runtime.getRuntime().exec(command);
            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    //add a function to add an audio file to a video file

    public static void addAudioToVideo(String inputVideo, String inputAudio, String outputVideo) {
        String command = "ffmpeg -i " + inputVideo + " -i " + inputAudio + " -c:v copy -c:a aac -strict experimental " + outputVideo;
        try {
            Process process = Runtime.getRuntime().exec(command);
            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

}


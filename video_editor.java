import org.opencv.core.*;
import org.opencv.videoio.*;
import java.io.*;
import java.util.Random;

class Main {
    public static String frame_clipper(String input_file, int start_time, int end_time) {
    // Open the input video file
    VideoCapture cap = new VideoCapture(input_file);

        // Get the frames per second (fps) of the video
        double fps = cap.get(Videoio.CAP_PROP_FPS);

        // Compute the starting and ending frame numbers
        int start_frame = (int)(start_time * fps);
        int end_frame = (int)(end_time * fps);

        // Define the codec and create the output video file
        int fourcc = VideoWriter.fourcc('m', 'p', '4', 'v');
        String temp_file = "output_file_clipped.mp4";
        Size frameSize = new Size((int)cap.get(3), (int)cap.get(4));
        VideoWriter out = new VideoWriter(temp_file, fourcc, fps, frameSize, true);

        // Read the frames of the video
        int current_frame = 0;
        Mat frame = new Mat();
        while (cap.read(frame)) {
            if (current_frame >= start_frame && current_frame <= end_frame) {
                //frame = cv2.rotate(frame, cv2.ROTATE_180)
                out.write(frame);
            }
            current_frame++;
        }

        // Release the resources
        cap.release();
        out.release();
        String path = System.getProperty("user.dir");
        String output_video = path + '/' + temp_file;
        return output_video;
    }
    //convert the frames to 9:16 aspect ratio

    public static String frame_converter(String input_file) {
        // Open the input video file
        VideoCapture cap = new VideoCapture(input_file);

        // Get the frames per second (fps) of the video
        double fps = cap.get(Videoio.CAP_PROP_FPS);

        // Define the codec and create the output video file
        int fourcc = VideoWriter.fourcc('m', 'p', '4', 'v');
        String temp_file = "output_file_converted.mp4";
        Size frameSize = new Size((int)cap.get(3), (int)cap.get(4));
        VideoWriter out = new VideoWriter(temp_file, fourcc, fps, frameSize, true);

        // Read the frames of the video
        Mat frame = new Mat();
        while (cap.read(frame)) {
            //frame = cv2.rotate(frame, cv2.ROTATE_180)
            out.write(frame);
        }

        // Release the resources
        cap.release();
        out.release();
        String path = System.getProperty("user.dir");
        String output_video = path + '/' + temp_file;
        return output_video;
    }

    // MIX AUDIO AND VIDEO

    public static String audio_video_mixer(String input_video, String input_audio) {
        // Open the input video file
        VideoCapture cap = new VideoCapture(input_video);

        // Get the frames per second (fps) of the video
        double fps = cap.get(Videoio.CAP_PROP_FPS);

        // Define the codec and create the output video file
        int fourcc = VideoWriter.fourcc('m', 'p', '4', 'v');
        String temp_file = "output_file_mixed.mp4";
        Size frameSize = new Size((int)cap.get(3), (int)cap.get(4));
        VideoWriter out = new VideoWriter(temp_file, fourcc, fps, frameSize, true);

        // Read the frames of the video
        Mat frame = new Mat();
        while (cap.read(frame)) {
            //frame = cv2.rotate(frame, cv2.ROTATE_180)
            out.write(frame);
        }

        // Release the resources
        cap.release();
        out.release();
        String path = System.getProperty("user.dir");
        String output_video = path + '/' + temp_file;
        return output_video;
    }

    public static void main(String[] args) {
        System.out.println("hello world");

        // Define the input and output files
       //String inp = args[0];
        String inp = "/Users/aviralchandra/Desktop/RawReels/test.mp4";
        //out = "output_video.mp4"

        // Define the start and end times for the trim (in seconds)
        //int start = Integer.parseInt(args[1]);
        int start = Integer.parseInt(10);
        int end = Integer.parseInt(15);

        //int end = Integer.parseInt(args[2]);
        String audio_directory = "/Users/aviralchandra/Desktop/StockAudio";
    }
}
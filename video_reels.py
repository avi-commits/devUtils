#!/usr/bin/python

from moviepy.editor import VideoFileClip
import cv2

input_file = "landscape_video.mp4"
output_file = "landscape_video_edited.mp4"

# Define the start and end times for the trim
start_time = "00:00:51"
end_time = "00:00:59"

# Load the video file
clip = VideoFileClip(input_file)

'''
# Trim the video between the start and end times
trimmed_clip = clip.subclip(start_time, end_time)
'''

# Trim the video between the start and end times
trimmed_clip = clip.set_start(start_time).set_end(end_time)

# Write the trimmed video to the output file
trimmed_clip.write_videofile(output_file)

'''

# Open the video file
video = cv2.VideoCapture(output_file)

# Get the video frame dimensions
frame_width = int(video.get(3))
frame_height = int(video.get(4))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("insta_reels_edited.mp4", fourcc, 30, (int(frame_height * 9/16), frame_height), isColor=True)

# Read frames from the video
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Crop the frame to 9:16 aspect ratio
    frame = frame[0:frame_height, int((frame_width - frame_height*(9/16))/2):int((frame_width + frame_height*(9/16))/2)]
    # Write the frame to the output file

    # rotating frame by 180

    frame = cv2.rotate(frame, cv2.ROTATE_180)    

    out.write(frame)

# Release the video writer and video capture objects
out.release()
video.release()

'''


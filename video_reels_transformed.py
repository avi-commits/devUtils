import cv2
import numpy as np

# Open the video file
video = cv2.VideoCapture("landscape_video.mp4")

# Get the video frame dimensions
frame_width = int(video.get(3))
frame_height = int(video.get(4))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("insta_reels_rotated.mp4", fourcc, 30, (int(frame_height * 9/16), frame_height), isColor=True)

# Get the rotation matrix
center = (frame_width/2, frame_height/2)
matrix = cv2.getRotationMatrix2D(center, 270, 1.0)

# Read frames from the video
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Crop the frame to 9:16 aspect ratio
    frame = frame[0:frame_height, int((frame_width - frame_height*(9/16))/2):int((frame_width + frame_height*(9/16))/2)]
    # Rotate the frame
    frame = cv2.warpAffine(frame, matrix, (frame_width, frame_height))
    # Write the frame to the output file
    out.write(frame)

# Release the video writer and video capture objects
out.release()
video.release()


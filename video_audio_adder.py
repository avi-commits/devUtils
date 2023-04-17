import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip

# Define the input video, audio directory and output video files
input_video = "input_video.mp4"
audio_dir = "/Users/aviralchandra/Desktop/StockAudio"
output_video = "output_video.mp4"

import os
import random
import cv2
import numpy as np
import soundfile as sf

# Get a list of all audio files in the directory
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

# Pick a random audio file
random_audio = random.choice(audio_files)

# Build the full path to the audio file
audio_path = os.path.join(audio_dir, random_audio)

# Read the audio file
audio_data, sample_rate = sf.read(audio_path)

# Open the video file
cap = cv2.VideoCapture(input_video)

# Get video codec information
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

# Get video frames per second (fps)
fps = cap.get(cv2.CAP_PROP_FPS)

# Get video frame size
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Create the video writer object
out = cv2.VideoWriter(output_video, fourcc, fps, frame_size, isColor=True)

# Iterate over the frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video writer object
out.release()

# Release the video capture object
cap.release()

# Close all the opened windows
cv2.destroyAllWindows()

# Write the audio data to the video file
with open(output_video, 'ab') as f:
    f.write(audio_data.tobytes())

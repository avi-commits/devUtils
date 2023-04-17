import cv2
import sys
import os
import random

# Define the input and output files
input_file = sys.argv[1]
output_file = "output_video.mp4"

# Define the start and end times for the trim (in seconds)
start_time = int(sys.argv[2])
end_time = int(sys.argv[3])

# Open the input video file
cap = cv2.VideoCapture(input_file)

# Get the frames per second (fps) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Compute the starting and ending frame numbers
start_frame = start_time * fps
end_frame = end_time * fps

# Define the codec and create the output video file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

# Read the frames of the video
current_frame = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break

    if current_frame >= start_frame and current_frame <= end_frame:
        #frame = cv2.rotate(frame, cv2.ROTATE_180)
        out.write(frame)

    current_frame += 1


# Release the resources
cap.release()
out.release()

#Conversion to reels#


# Open the video file
video = cv2.VideoCapture(output_file)

# Get the video frame dimensions
frame_width = int(video.get(3))
frame_height = int(video.get(4))

# Define the codec and create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out_path = str(random.randint(0,1000000))+"_insta_reels_edited.mp4"
out = cv2.VideoWriter(out_path, fourcc, 30, (int(frame_height * 9/16), frame_height), isColor=True)

# Read frames from the video
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Crop the frame to 9:16 aspect ratio
    frame = frame[0:frame_height, int((frame_width - frame_height*(9/16))/2):int((frame_width + frame_height*(9/16))/2)]
    # Write the frame to the output file

    # rotating frame by 180

    #frame = cv2.rotate(frame, cv2.ROTATE_180)    

    out.write(frame)

# Release the video writer and video capture objects
out.release()
video.release()

os.remove(output_file)

#using ai to generate music
'''
import openai
import requests
import moviepy.editor as mp

# Define the input and output files
#input_video = "input_video.mp4"
input_video = output_file
output_video = "output_video.mp4"

# Get the API key
openai.api_key = "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"
key = openai.api_key

# Define the parameters for the generation
prompt = (f"generate a 30 seconds EDM chorus")

# Make the API request
response = requests.post(
    "https://api.openai.com/v1/engines/davinci-codex/completions",
    json={
        "prompt": prompt,
        "max_tokens": 1024,
        "stop": "."
    },
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
)

# Save the generated audio file
with open("edm_chorus.wav", "wb") as f:
    f.write(response.content)

from pydub import AudioSegment

# Convert the generated audio file from wav to mp3
audio = AudioSegment.from_wav("edm_chorus.wav")
audio.export("edm_chorus.mp3", format="mp3")


# Load the input video and the generated audio
video = mp.VideoFileClip(input_video)
#audio = mp.AudioFileClip("edm_chorus.wav")
audio = mp.AudioFileClip("edm_chorus.mp3")

# Add the background audio to the video
final_video = mp.CompositeVideoClip([video.set_audio(audio)])

# Write the final video to the output file
final_video.write_videofile(output_video)
'''


'''
# Define the input video, audio directory and output video files
input_video = out_path
audio_dir = "/Users/aviralchandra/Desktop/StockAudio"
output_video = "output_video_with_audio.mp4"

# Get a list of all audio files in the directory
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

# Pick a random audio file
random_audio = random.choice(audio_files)

print(random_audio)


import subprocess
# Build the full path to the audio file

audio_path = os.path.join(audio_dir, random_audio)
#audio_path = audio_dir+'/'+"clipped_audio.mp3"

subprocess.run(["ffmpeg", "-i", input_video, "-i", audio_path, "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", output_video])
'''

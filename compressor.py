#!/usr/bin/python

import os
import subprocess
from pathlib import Path

def compress_video(input_file, output_file, bitrate='500k'):
    subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-b:v', bitrate, '-movflags', '+faststart', output_file])

input_dir = '/Users/aviralchandra/Desktop/input_videos'
output_dir = '/Users/aviralchandra/Desktop/output_videos'
bitrate = '1000k'

'''
for file in os.listdir(input_dir):
    filename, file_extension = os.path.splitext(file)
    if file_extension in ['.mp4', '.mkv', '.avi', '.mov']:
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, f"compressed_{filename}{file_extension}")
        compress_video(input_file, output_file, bitrate)
'''

input = '/Users/aviralchandra/Desktop/RawReels/intro_in.mp4'
output = '/Users/aviralchandra/Desktop/RawReels/intro_out.mp4'

compress_video(input, output, bitrate)
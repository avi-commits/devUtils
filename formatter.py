import ffmpeg

def create_h264_video(input_file, output_file, bitrate='1000k'):
    stream = ffmpeg.input(input_file)
    stream = ffmpeg.output(stream, output_file, c='libx264', b=bitrate)
    ffmpeg.run(stream)

input_file = '/Users/aviralchandra/Desktop/input.mp4'
output_file = '/Users/aviralchandra/Desktop/output2.mp4'
create_h264_video(input_file, output_file)

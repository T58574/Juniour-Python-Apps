import moviepy.editor
from pathlib import Path


def convert_mp4_to_mp3(mp4_file):
    video_path = Path(mp4_file)
    video = moviepy.editor.VideoFileClip(f'{video_path}')
    audio = video.audio
    audio.write_audiofile(f'{video_path.stem}.mp3')


convert_mp4_to_mp3('path/to/video.mp4')

from pytube import YouTube
import moviepy.editor
from time import sleep as s
from pathlib import Path


def convert_mp4_to_mp3(mp4_file, mp3_file):
    video = moviepy.editor.VideoFileClip(f'{mp4_file}')
    audio = video.audio
    audio.write_audiofile(mp3_file)
    print('\nmp3 converting finish.\n')
    audio.close()
    video.close()
    file = Path(mp4_file)
    file.unlink()


def download_youtube():
    url = str(input('Url -> '))
    yt = YouTube(url)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
    mp4_file = f'{yt.title}.mp4'
    mp3_file = f'Converted - {yt.title}.mp3'
    convert_mp4_to_mp3(mp4_file, mp3_file)


download_youtube()

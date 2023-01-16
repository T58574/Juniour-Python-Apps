from pytube import YouTube

def download_youtube(url):
    yt = YouTube(url)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download('.\\cache\\')
    print(f'\nFinished downloading:  {yt.title}')

download_youtube('Your url')
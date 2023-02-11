from pytube import YouTube

def download_youtube():
    url = str(input('Url -> '))
    yt = YouTube(url)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
    yttitle = yt.title
    yttitle = yttitle.replace('@/*#!$%^?\[]-_)+=;`~.,<>\'"|', '')

download_youtube()

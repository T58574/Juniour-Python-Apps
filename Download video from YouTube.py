from pytube import YouTube

def download_youtube():
    url = str(input('Url ->\n\n'))
    yt = YouTube(url)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download()
    print('Success\n')

while True:
    download_youtube()
    more = input('more? y/n ->\n\n')
    if more == 'y':
        download_youtube()
    elif more == 'n':
        pass
    else: break


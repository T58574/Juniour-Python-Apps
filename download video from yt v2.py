import subprocess

url = str(input('Url -> '))
comm1 = f'pytube {url} -a'
subprocess.call(comm1, shell=True)

# Need install pytube

from pytube import YouTube

# chinese video
link = "https://youtu.be/UTOQdej0Mus?si=aOmOqedANCravVA2"


yt = YouTube(link)
yt.streams.filter(only_audio=True).first().download()

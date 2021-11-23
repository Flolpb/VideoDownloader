from pytube import YouTube
url = input("Lien de votre vidéo youtube: ")
video = YouTube(url)
videos = video.streams.filter(file_extension = "mp4")
stream = videos.get_by_resolution("1080p")
if(stream == None):
    stream = videos.get_highest_resolution()
print("{} Downloading...".format(stream.title))
stream.download("videos")
print("{} Downloaded...".format(stream.title))
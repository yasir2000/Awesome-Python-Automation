from pytube import YouTube

link = input("Enter the link: ")
video = YouTube(link)
stream = video.streams.first()
stream.download()
# Basic attempt at establishing pytube; requires pytube

from pytube import YouTube
link = input("Please input your youtube URL here: ")
yt = YouTube(link)
videoservice = yt.streams.all()

# Now it might be useful to find some way of numerating or showing the potential list of videos and video formats?

video = list(enumerate(videoservice))
for i in video:
    print(i)

print("Please select the format")
option = int(input("Enter your option: "))
video_option = videoservice[option]
video_option.download()

# Classy closing statement

print("Your download has been successfully completed")

from pytube import YouTube #pip install pytube

link = input("Enter YouTube video URL: ")

yt = YouTube(link)

#will stream all the format available for the video
videos = yt.streams.all() 

# will index all formats in list starting with zero
video = list(enumerate(videos))

for i in video:
    print(i) #print all the formats with proper index

print("Choose a format you wish to download")
dl_option = int(input(" Enter the option: ")) #Ask user which format to download
dl_video = videos[dl_option]
dl_video.download() #to download the selected option

""" result = yt.streams.get_highest_resolution()

result.download() """

print(" Downloaded successfully! ")

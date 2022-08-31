    #import the module
from pytube import YouTube

#the link of the video which we need to download
link = "https://youtu.be/D8rlcLH0pqk"

#call the youtube function passing the link as parameter and all the data related to link will go into variable yt
yt= YouTube(link)

#creating a variable to store the detail of video streaming
video_stream= yt.streams

#to convert the details of streaming into list
#using enumerate to get the index no of the list through which we can download the video
n = list(enumerate(video_stream))

#using for loop to print the list
for i in n:
    print(i)
print()
#take an input from which stream we want to download the video in
res= int(input("Enter the index number of the quality of video you want to download in "))
video_stream[res].download()

print("Congrats!! Your video has been downoaded successfully!!")

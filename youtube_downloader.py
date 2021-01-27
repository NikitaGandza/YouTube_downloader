import pytube

url = input("Please enter URL: ")
youtube = pytube.YouTube(url)

# To check all available streams with itags
streams = youtube.streams.all()
for stream in streams:
    print(stream) 

# To download video by itag 
itag = input("Please enter itag:")
video = youtube.streams.get_by_itag(itag)
video.download('/Users/nikitagandza/Desktop') #path

print("Video is downloaded!") 

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pytube

def streams():
    url = link.get()
    youtube = pytube.YouTube(url)
    streams = youtube.streams.all()
    for stream in streams:
        print(stream) 
    info['text'] = f'{[streams]}'

root = Tk()
root.title("YouTube downloader")
root.geometry("1000x500+50+450")
root.resizable(False, False)



frame = Frame(root, bg='#851e3e')
frame.place(relheight = 1, relwidth = 1)

link = Entry(frame, bg='white')
link.pack()

btn = Button(frame, text = 'Streams', background ='#851e3e', command = streams)
btn.pack()

info = Label(frame, text='Streams', bg='#ffb700', font=40)
info.pack()

btn1 = Button(frame, text = 'Download', command = streams)
btn1.pack()

#dropdown

#choices = ["1080p", "720p", "480p", "360p", "240p", "144p", "audio only"]
#dropdown = ttk.Combobox(root, values=choices)
#dropdown.grid()

root.mainloop()


import os
import tkinter as tk
from tkinter import SINGLE, END, ACTIVE
from pygame import mixer

from PIL import ImageTk, Image

root = tk.Tk()
root.title('Music Player')
root.geometry('460x400+390+100')
root.config(background='#ffffff')
root.resizable(0,0)

#Events
def playMusic():
    running = listbox.get(ACTIVE)
    running_songs['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pauseMusic():
    mixer.music.pause()

def resumeMusic():
    mixer.music.unpause()

def stopMusic():
    mixer.music.stop()

def prevMusic():
    playing = running_songs['text']
    index = songs.index(playing)
    newIndex = index - 1

    playing = songs[newIndex]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()

    listbox.select_set(newIndex)
    running_songs['text'] = playing

def forwardMusic():
    playing = running_songs['text']
    index = songs.index(playing)
    newIndex = index + 1

    playing = songs[newIndex]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)
    show()

    listbox.select_set(newIndex)
    running_songs['text'] = playing


#Frames
down_frame1 = tk.Frame(root, width=445, height=255, bg='#333333')
down_frame1.grid(row=2, column=0, padx=7, pady=8)

down_frame2 = tk.Frame(root, width=445, height=115, bg='#99ff99')
down_frame2.grid(row=3, column=0, padx=7, pady=5)

#ListBox
listbox = tk.Listbox(down_frame1, selectmode=SINGLE, font=('times 10 bold'), width=60, height=15, bg='#333333', fg='#ffffff')
listbox.grid(row=0, column=0)

s = tk.Scrollbar(down_frame1)
s.grid(row=0, column=1)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

#Images
img1 = Image.open('icons/1backward.png')
img1 = img1.resize((45, 45))
img1 = ImageTk.PhotoImage(img1)
previous = tk.Button(down_frame2, image=img1, padx=8, pady=6, command=prevMusic)
previous.place(x=65, y=45)

img2 = Image.open('icons/2play.png')
img2 = img2.resize((45, 45))
img2 = ImageTk.PhotoImage(img2)
play = tk.Button(down_frame2, image=img2, padx=8, pady=6, command=playMusic)
play.place(x=116, y=45)

img3 = Image.open('icons/3forward.png')
img3 = img3.resize((45, 45))
img3 = ImageTk.PhotoImage(img3)
forward = tk.Button(down_frame2, image=img3, padx=8, pady=6, command=forwardMusic)
forward.place(x=167, y=45)

img4 = Image.open('icons/4pause.png')
img4 = img4.resize((45, 45))
img4 = ImageTk.PhotoImage(img4)
pause = tk.Button(down_frame2, image=img4, padx=8, pady=6, command=pauseMusic)
pause.place(x=218, y=45)

img5 = Image.open('icons/5resume.png')
img5 = img5.resize((45, 45))
img5 = ImageTk.PhotoImage(img5)
forward = tk.Button(down_frame2, image=img5, padx=8, pady=6, command=resumeMusic)
forward.place(x=269, y=45)

img6 = Image.open('icons/6stop.png')
img6 = img6.resize((45, 45))
img6 = ImageTk.PhotoImage(img6)
forward = tk.Button(down_frame2, image=img6, padx=8, pady=6, command=stopMusic)
forward.place(x=320, y=45)

running_songs = tk.Label(down_frame2, text="Choose a Song", font=("times 12"), width=46, height=1, padx=10, bg='#333333', fg='#ffffff')
running_songs.place(x=3.3, y=1.8)


os.chdir(r'C:\Users\vansh\Music\music')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)

show()

mixer.init()
music_state = tk.StringVar()
music_state.set("Choose One !")

root.mainloop()
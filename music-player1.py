import os
import pygame
from mutagen.id3 import ID3,TIT2
import tkinter
from tkinter.filedialog import askdirectory 


root=tkinter.Tk()
root.minsize(300,300)

listOfSongs=[]
realNames=[]


v=tkinter.StringVar()
songLabel=tkinter.Label(root,textvariable=v,width=35)
index=0


# def playSongs(event):
#     global index
#     index=0
#     pygame.mixer.music.load(listOfSongs[index])
#     pygame.mixer.music.play()
#     updatelabel()

def nextSong(event):
    global index
    index+=1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevSong(event):
    global index
    index-=1
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopSong(event):
    pygame.mixer.music.stop()
    v.set("")
    
    
def updatelabel():
    global index
    v.set(realNames[index])
    # return listOfSongs



def directoryChooser():
    directory=askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir=os.path.realpath(files) #menyesuaikan-letak-folder
            audio=ID3(realdir)
            # audio.add(TIT2(encoding=3,text=u"Title"))
            # audio.save(realdir)
            realNames.append(audio['TIT2'].text[0])
            
            #audio.save(v2_version=3) 
            listOfSongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[0])
    # pygame.mixer.music.play()

directoryChooser() #calling-function





label=tkinter.Label(root,text="Music Player")
label.pack()

listbox=tkinter.Listbox(root)
listbox.pack()

# playSongsButton=tkinter.Button(root,text="Play")
# playSongsButton.pack()

nextButton=tkinter.Button(root,text="Next Song")
nextButton.pack()

previousButton=tkinter.Button(root,text="Previous Song")
previousButton.pack()

stopButton=tkinter.Button(root,text="Stop Button")
stopButton.pack()


# playSongsButton.bind("Button-1",playSongs)
nextButton.bind("<Button-1>",nextSong)
previousButton.bind("<Button-1>",prevSong)
stopButton.bind("<Button-1>",stopSong)

# songlabel.pack()




#listOfSongs.reverse()
realNames.reverse()
for items in listOfSongs:
    listbox.insert(0,items)
# listOfSongs.reverse()
realNames.reverse()

songLabel.pack()

root.mainloop()

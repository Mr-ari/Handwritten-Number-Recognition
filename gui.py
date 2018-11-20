from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

def user_browse():
    imgfile = askopenfilename(initialdir="/home/ari/",title="Select the Image File",filetypes=(("JPEG","*.jpg"),("PNG","*.png")))
    if imgfile:
        try:
            print(imgfile)
        except:  # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % imgfile)
        return

def user_exit():
    exit()

window = Tk()
#creating a frame of size 500x500
window.geometry("500x500")

#set the frame title
window.title("Handwritten Numbers Recognition")

#setting up the backgroud

background_img = PhotoImage(file = "Numbers.png")
background_lb = Label (window,image = background_img)
background_lb.place(x=0,y=0,relheight=1,relwidth=1)

#creating two buttons ---- 1.for browsing the file ---- 2.for quit the app
BrowseButton = Button(window,text="Browse The Image File",fg="white",bg="black",command=user_browse,activebackground="green",activeforeground="white")
QuitButton = Button (window,text = "Quit",fg="white",bg="black",activebackground="red",activeforeground="white",command=user_exit)

#placing those buttons in the frame
QuitButton.place(x=210,y=235)
BrowseButton.place(x=160,y=190)

window.mainloop()
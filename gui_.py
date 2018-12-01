from tkinter import *
import NumberRecog as nr
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

def user_browse():
    global InputedImageFile
    InputedImageFile = askopenfilename(initialdir="Test_Images/",title="Select the Image File",filetypes=(("JPEG","*.jpg"),("PNG","*.png")))
    if str(type(InputedImageFile)) != "<class 'str'>":
        InputedImageFile="No Input File Selected"
    T.config(state=NORMAL)
    T.delete(1.0,END)
    T.insert(INSERT,InputedImageFile)
    T.config(state=DISABLED)
def user_exit():
    exit()

def submit_button():
    global InputedImageFile
    nr.Main(InputedImageFile)


def foo():
    print("hello")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = img_copy.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    background.config(image=photo)
    background.image = photo  # avoid garbage collection



InputedImageFile = "No Input File Selected"
window = Tk()
#creating a frame of size 500x500
window.geometry("600x350")

#set the frame title
window.title("Handwritten Numbers Recognition")

#setting up the backgroud

img = Image.open("Datas/background.png")
img_copy = img.copy()
photo = ImageTk.PhotoImage(img)
background = Label (window,image = photo)
background.bind('<Configure>', resize_image)
background.pack(fill=BOTH, expand = YES)

T = Text(window, height=1)
T.pack()
T.insert(INSERT, InputedImageFile)
T.config(state=DISABLED)
T.place(relx=0.5,rely=0.6,anchor= CENTER)

#creating two buttons ---- 1.for browsing the file ---- 2.for quit the app
BrowseButton = Button(window,text="Browse The Image File",fg="white",bg="black",command=user_browse,activebackground="white",activeforeground="black")
QuitButton = Button (window,text = "Quit",fg="white",bg="red",activebackground="black",activeforeground="white",command=user_exit,width=4)
SubmitButton = Button(window,text = "Submit",fg="white",bg="green",activebackground="black",activeforeground="white",command=submit_button)

#placing those buttons in the frame
QuitButton.place(relx=0.9, rely=1.0,anchor=SW)
SubmitButton.place(relx=0.0, rely=1.0,anchor=SW)
BrowseButton.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()
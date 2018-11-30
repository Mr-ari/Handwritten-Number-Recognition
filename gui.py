"""
-----------------------------------------------------------------------------------------------------------

            Project Name : User Interface for the Number Detection
            Date         : 21/11/2018 21:42 TUE
            Author       : Arijit Ghosh

-----------------------------------------------------------------------------------------------------------

"""


from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget      
        self.master.title("GUI")

        #setting up the background image for the frame
        self.image = Image.open("background.jpeg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        self.pack(fill=BOTH,expand=1)
        # allowing the widget to take the full space of the root window


        #setting up the buttons
        # creating a button instance
        BrowseButton = Button(self, text="Browse The Image File", fg="white", bg="black", command=self.user_browse,
                              activebackground="green", activeforeground="white")
        QuitButton = Button(self, text="Quit", fg="white", bg="black", activebackground="red",
                            activeforeground="white", command=self.user_exit)

        # placing those buttons in the frame
        QuitButton.place(relx=0.5, rely=0.5,anchor = CENTER)
        BrowseButton.place(relx=0.5, rely=0.4,anchor=CENTER)

    def get_imagefile(self):
        return self.imgfile

	#user presses the browse button
    def user_browse(self):
        self.imgfile = askopenfilename(initialdir="/home/ari/PycharmProjects/NumberDetectionGui/Test_Images/", title="Select the Image File",
                                  filetypes=(("JPEG", "*.jpg"), ("PNG", "*.png")))
        if self.imgfile:
            try:
                print(self.imgfile)
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % self.imgfile)
            return
	
	#user presses the exit button
    def user_exit(self):
        exit()

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)






if __name__ == "__main__":
    root = Tk()
    #size of the window
    root.geometry("500x500")

    app = Window(root)
    root.mainloop()


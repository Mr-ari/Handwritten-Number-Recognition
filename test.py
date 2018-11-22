import gui
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename


def open_file(filename):
    print("filename is +"+filename)


#overrinding the user_browse method

class Window_(gui.Window):
    def user_browse(self):
        self.imgfile = askopenfilename(initialdir="/home/ari/PycharmProjects/NumberDetectionGui/Test_Images/",
                                       title="Select the Image File",
                                       filetypes=(("JPEG", "*.jpg"), ("PNG", "*.png")))
        if self.imgfile:
            try:
                print(self.imgfile)
            except:  # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % self.imgfile)
            return

        open_file(self.imgfile)


root = Tk()
root.geometry("500x500")
app = Window_(root)
mainloop()
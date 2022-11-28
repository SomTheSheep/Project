import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

top = tkinter.Tk()
store = tkinter.StringVar()
top.geometry('1920x1080')

top.grid_columnconfigure(0, weight = 1)
top.title("PESU")
photo = Image.open('download.png')
realphoto = photo.resize((404,126))
finalphoto = ImageTk.PhotoImage(realphoto)


quack = Label(image = finalphoto)
quack.grid(column = 0, row = 0)


profile = Image.open('pfp.png')
realprofile = profile.resize((126,126))
finalimg = ImageTk.PhotoImage(realprofile)
#profilelabel = Label(image = finalimg)
#profilelabel.grid(column = 1, row = 0)

attendance = Image.open('attendance.png')
attendance = attendance.resize((252,46))
att = ImageTk.PhotoImage(attendance)

results = Image.open('results.png')
res = ImageTk.PhotoImage(results)




l2 = tkinter.Label(top, text ="")
l2.grid()


en = tkinter.Entry(top, textvariable = store)
en.grid()


def Yep():
    
    out = en.get()
    l2.configure(text=out)


B = tkinter.Button(top, image = att, command=Yep)
B.grid()

def ex():
    tkinter.messagebox.showinfo(title = 'Profile', message = "Button serves no function as of now")

User = tkinter.Button(top, image = finalimg , command = ex )
User.grid(column = 1, row = 0)

re = tkinter.Button(top, image = res, command = ex)
re.grid()



top.mainloop()

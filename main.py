import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import im


top = tkinter.Tk()
store = tkinter.StringVar()
top.geometry('1920x1080')

top.grid_columnconfigure(0, weight = 1)
top.title("PESU")

finalphoto = ImageTk.PhotoImage(im.realphoto)



quack = Label(image = finalphoto)
quack.grid(column = 0, row = 0)



finalimg = ImageTk.PhotoImage(im.profile)



att = ImageTk.PhotoImage(im.attphoto)


res = ImageTk.PhotoImage(im.results)




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

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

en_font = ('Freestyle Script', 28)
en_font2 = ('Freestyle Script', 26)
en = tkinter.Label(top, text = "WELCOME   TO   THE   STUDENT   DATABASE", font = en_font)
en.grid()

EN2 = tkinter.Label(top, text = "Please click on your desired icon", font = en_font2)
EN2.grid()

tkinter.Label(top, text='').grid()


def Yep():
    
    out = en.get()
    l2.configure(text=out)





def ex():
    tkinter.messagebox.showinfo(title = 'In Progress', message = "Button serves no function as of now")
B = tkinter.Button(top, image = att, command=ex)
B.grid()

User = tkinter.Button(top, image = finalimg , command = ex )
User.grid(column = 1, row = 0)

tkinter.Label(top, text='').grid()

re = tkinter.Button(top, image = res, command = ex)
re.grid()



top.mainloop()

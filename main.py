import tkinter
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import im



top = tkinter.Tk()
store = tkinter.StringVar()
top.geometry('1920x1080')

top.grid_columnconfigure(0, weight = 1)
top.title("DATABASE")

finalphoto = ImageTk.PhotoImage(im.photo)



quack = Label(image = finalphoto)
quack.grid(column = 0, row = 0)



finalimg = ImageTk.PhotoImage(im.profile)



att = ImageTk.PhotoImage(im.attphoto)


res = ImageTk.PhotoImage(im.results)

time = ImageTk.PhotoImage(im.timetable)
timeg = ImageTk.PhotoImage(im.timetableex)

cal = ImageTk.PhotoImage(im.calendar)




l2 = tkinter.Label(top, text ="")
l2.grid()

en_font = ('Freestyle Script', 28)
en_font2 = ('Freestyle Script', 26)
en = tkinter.Label(top, text = "WELCOME   TO   THE   STUDENT   DATABASE", font = en_font)
en.grid()

EN2 = tkinter.Label(top, text = "Please click on your desired icon", font = en_font2)
EN2.grid()

tkinter.Label(top, text='').grid()


def ex():
    tkinter.messagebox.showinfo(title = 'In Progress', message = "Button serves no function as of now")
B = tkinter.Button(top, image = att, command=ex)
B.grid()

def Prof():
     
    
    newWindow = Toplevel(top)
 
    
    newWindow.title("Student Info")
 
    
    newWindow.geometry("400x400")
 
    
    Label(newWindow,
          text =" Name: \nUSN:").grid()
User = tkinter.Button(top, image = finalimg , command = Prof )
User.grid(column = 1, row = 0)


def t():
    new = Toplevel(top)
 
    
    new.title("Time Table")
 
    
    new.geometry("1242x663")
 
    
    Label(new,
          image=timeg).grid()

tkinter.Label(top, text='').grid()

re = tkinter.Button(top, image = res, command = ex)
re.grid()

tkinter.Label(top, text='').grid()

tt = tkinter.Button(top, image = time, command = t)
tt.grid()

tkinter.Label(top, text ='').grid()
def caldisplay():
    newnew = Toplevel(top)
    menubar = Menu(newnew)  
    menubar.add_command(label="Monday", command=print("True"))
    menubar.add_command(label="Quit!", command=newnew.quit)  
  
    # display the menu  
    newnew.config(menu=menubar)  
cale = tkinter.Button(top, image = cal, command = caldisplay)
cale.grid()



top.mainloop()

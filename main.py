import tkinter
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import im

import login



top = tkinter.Tk()
store = tkinter.StringVar()
top.geometry('1920x1080')

top.grid_columnconfigure(0, weight = 1)
top.title("Database")

finalphoto = ImageTk.PhotoImage(im.photo)



quack = Label(top, image = finalphoto)
quack.grid(column = 0, row = 0)



finalimg = ImageTk.PhotoImage(im.profile)



att = ImageTk.PhotoImage(im.attphoto)


res = ImageTk.PhotoImage(im.results)

time = ImageTk.PhotoImage(im.timetable)
timeg = ImageTk.PhotoImage(im.timetableex)

mon = ImageTk.PhotoImage(im.monday)
tues = ImageTk.PhotoImage(im.tuesday)
wed = ImageTk.PhotoImage(im.wednesday)
thurs = ImageTk.PhotoImage(im.thursday)
fri = ImageTk.PhotoImage(im.friday)

cal = ImageTk.PhotoImage(im.calendar)

jan = ImageTk.PhotoImage(im.january)
feb = ImageTk.PhotoImage(im.february)

st = ImageTk.PhotoImage(im.p)




l2 = tkinter.Label(top, text ="")
l2.grid()

en_font = ('Freestyle Script', 28)
en_font2 = ('Freestyle Script', 26)
en_font3 = ('Arial Black', 26)
en = tkinter.Label(top, text = "WELCOME   TO   THE   STUDENT   DATABASE", font = en_font)
en.grid()

EN2 = tkinter.Label(top, text = "Please click on your desired option", font = en_font2)
EN2.grid()

tkinter.Label(top, text='').grid()


def ex():
    tkinter.messagebox.showinfo(title = 'In Progress', message = "Button serves no function as of now")
def atte():
    newnewnew = Toplevel(top)
    newnewnew.title("Attendance")
    newnewnew.geometry('200x40')
    Label(newnewnew, text = "You have attended 91/100 classes").grid()
    Label(newnewnew, text = "Your attendance is: 91%").grid()

B = tkinter.Button(top, image = att, command=atte)
B.grid()

def Prof():
     
    
    newWindow = Toplevel(top)
 
    
    newWindow.title("Student Info")
    
 
    
    newWindow.geometry("300x300")
    Label(newWindow, image = st).grid()
 
    
    tkinter.Label(newWindow,text ="Name:Rohan \nUSN:SC2022R01").grid()
User = tkinter.Button(top, image = st , command = Prof )
User.grid(column = 1, row = 0)



def t():
    def monday():
        
        tkinter.Label(new, text = 'Monday', font = en_font3).grid(row = 0, column = 0)
        
        tkinter.Label(new, image = mon).grid(row = 1, column = 0)
    def tuesday():
        
        tkinter.Label(new, text = 'Tuesday', font = en_font3).grid(row = 0, column = 0)
        tkinter. Label(new, image = tues).grid(row = 1, column = 0)
    def wednesday():
        tkinter.Label(new, text = 'Wednesday', font = en_font3).grid(row = 0, column = 0)
        tkinter.Label(new, image = wed).grid(row = 1, column = 0)
    def thursday():
        tkinter.Label(new,text = 'Thursday', font = en_font3).grid(row = 0, column = 0)
        tkinter.Label(new, image = thurs).grid(row = 1, column = 0)
    def friday():
        tkinter.Label(new, text = 'Friday', font = en_font3).grid(row = 0, column = 0)
        tkinter.Label(new, image = fri).grid(row = 1, column = 0)
    
        

    new = Toplevel(top)
    new.columnconfigure(0, weight = 1)
    new.title('Time Table')
    new.geometry('1920x1080')
    menubar = Menu(new)  
    menubar.add_command(label="Monday", command=monday)
    menubar.add_command(label="Tuesday", command=tuesday)  
    menubar.add_command(label='Wednesay', command = wednesday)
    menubar.add_command(label='Thursday', command=thursday)
    menubar.add_command(label='Friday', command=friday)
    menubar.add_command(label="Quit!", command=new.destroy)
    
    
  
    # display the menu  
    new.config(menu=menubar) 

tkinter.Label(top, text='Attendance', font = en_font2).grid()


def results():
    real = Toplevel(top)
    real.title('Results')
    real.geometry('250x200')
    Label(real, text="Your physics marks are: 75/100").grid()
    Label(real, text ="Your Maths marks are: 98/100").grid()
    Label(real, text ="Your Computer Science marks are: 91/100").grid()
    Label(real, text ="Your Chemistry marks are: 83/100").grid()
    Label(real, text = "Your Geography marks are: 96/100").grid()
    Label(real, text = "Your History marks are: 91/100").grid()
    Label(real, text = "Your 2nd language marks are: 98/100").grid()
re = tkinter.Button(top, image = res, command = results)
re.grid()
    

tkinter.Label(top, text='Exam Results', font = en_font2).grid()

tt = tkinter.Button(top, image = time, command = t)
tt.grid()

tkinter.Label(top, text ='Timetable', font = en_font2).grid()
def caldisplay():
    def ja():
        Label(newnew, image = jan).grid()
    newnew = Toplevel(top)
    newnew.geometry('900x400')
    newnew.title("Calendar of events")
    menubar = Menu(newnew)  
    menubar.add_command(label="January", command=ja)
    menubar.add_command(label="Quit!", command=newnew.destroy)  
  
    # display the menu  
    newnew.config(menu=menubar)  
cale = tkinter.Button(top, image = cal, command = caldisplay)
cale.grid()
tkinter.Label(top, text = 'Calendar', font = en_font2).grid()



top.mainloop() 

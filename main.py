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

mon = ImageTk.PhotoImage(im.monday)
tues = ImageTk.PhotoImage(im.tuesday)
wed = ImageTk.PhotoImage(im.wednesday)
thurs = ImageTk.PhotoImage(im.thursday)
fri = ImageTk.PhotoImage(im.friday)

cal = ImageTk.PhotoImage(im.calendar)

jan = ImageTk.PhotoImage(im.january)
feb = ImageTk.PhotoImage(im.february)




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
    new.geometry('1920x1080')
    menubar = Menu(new)  
    menubar.add_command(label="Monday", command=monday)
    menubar.add_command(label="Tuesday", command=tuesday)  
    menubar.add_command(label='Wednesay', command = wednesday)
    menubar.add_command(label='Thursday', command=thursday)
    menubar.add_command(label='Friday', command=friday)
    
    
  
    # display the menu  
    new.config(menu=menubar) 

tkinter.Label(top, text='Attendance', font = en_font2).grid()

re = tkinter.Button(top, image = res, command = ex)
re.grid()

tkinter.Label(top, text='Exam Results', font = en_font2).grid()

tt = tkinter.Button(top, image = time, command = t)
tt.grid()

tkinter.Label(top, text ='Timetable', font = en_font2).grid()
def caldisplay():
    newnew = Toplevel(top)
    menubar = Menu(newnew)  
    menubar.add_command(label="January", command=print("True"))
    menubar.add_command(label="Quit!", command=newnew.quit)  
  
    # display the menu  
    newnew.config(menu=menubar)  
cale = tkinter.Button(top, image = cal, command = caldisplay)
cale.grid()
tkinter.Label(top, text = 'Calendar', font = en_font2).grid()



top.mainloop() 

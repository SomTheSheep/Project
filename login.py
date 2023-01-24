from tkinter import *
from functools import partial


def validateLogin(username, password):
	import main


tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Student login')


usernameLabel = Label(tkWindow, text="Student Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  


passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)


loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()
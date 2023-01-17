from tkinter import *
from functools import partial

def Login(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return


tkWindow = Tk()  
tkWindow.geometry('1920x1080')  
tkWindow.title('Student login portal')


usernameLabel = Label(tkWindow, text="SRN")
usernameLabel.grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.grid(row=0, column=1)  


passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

Login = partial(Login, username, password)


loginButton = Button(tkWindow, text="Login", command=Login).grid(row=4, column=0)  

tkWindow.mainloop()
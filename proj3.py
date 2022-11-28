import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

root = tk.Tk()
root.geometry('400x400')
l1 = tk.Label(root, text = "YEP")
l1.grid()
txt = tk.Entry(root, width = 10)
txt.grid(column = 1, row = 0)
def clicked():
    res = "Welcome to "+txt.get()
    l1.configure(text=res)

bt = tk.Button(root, text = "Enter", command = clicked)
bt.grid()

root.mainloop()


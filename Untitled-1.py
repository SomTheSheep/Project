from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=5, row=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=10)
root.mainloop()
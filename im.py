import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk


attphoto = Image.open('att.png')
attphoto = attphoto.resize((85,85))


photo = Image.open('database3.png')
photo = photo.resize((230,128))


profile = Image.open('pfp.png')
profile = profile.resize((126,126))

results = Image.open('results.png')
results = results.resize((85,85))

timetable = Image.open('timetable.png')
timetable = timetable.resize((85,85))

    

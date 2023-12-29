# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

from tkinter import *
import tkinter as tk


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
# import tfModel_test as tf_test
global fn
fn = ""


root = tk.Tk()

root.title("Crop Prediction Using Machine Learning ")
root.geometry("1600x900")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()


bg = Image.open("image4.jpg")

# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=93, relwidth=1, relheight=1)

'''
bg = PhotoImage(file="image3.jpg")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
'''


img1 = ImageTk.PhotoImage(Image.open("image2.jpg"))

img2 = ImageTk.PhotoImage(Image.open("image3.jpg"))

img3 = ImageTk.PhotoImage(Image.open("image5.jpg"))

#img4 = ImageTk.PhotoImage(Image.open("img7.jpg"))

logo_label = tk.Label()
logo_label.place(x=60, y=250)

x = 1


def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img1)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
     # elif x ==4:
     #    logo_label.config(image=img4)
	x = x+1
	root.after(1000, move)

# calling the function
move()


#marquee
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=Canvas(root,bg="black")
canvas.pack()
text_var="Crop Prediction Using Machine Learning"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 100
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling


'''
def marquee_fun(widget, widget_w, widget_h, total_w, total_h, direction, speed, position=0):
    if direction=='right':
        if position>=total_w-widget_w:
            position=0
        position = position + speed
        widget.place(x=position)
        
    widget.after(10, lambda: marquee_fun(widget, widget_w, widget_h, total_w, total_h, direction, speed))

w = tk.Label(root, text="Crop Prediction Using Machine Learning",background="#17202A",foreground="white",font=("Times new roman",19,"bold"))
w.place(x=0,y=15, width=150, height=30)


w.after(100, lambda:marquee_fun(w, 150, 30, 500, 500, 'right', 2))

'''


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])

'''
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#17202A")
'''

wlcm=tk.Label(root,text="Crop Prediction",font=("Roboto",22,"bold"))
wlcm.place(x=350,y=270)




d2=tk.Button(root,text="Login",command=Login,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1100,y=350)


d3=tk.Button(root,text="Register",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1100,y=450)




root.mainloop()

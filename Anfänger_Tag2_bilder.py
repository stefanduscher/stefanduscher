#!/usr/bin/python
import tkinter, PIL
from tkinter import *
from PIL import ImageTk, Image
 
# Fester erstellen
tk = tkinter.Tk()
 
# Rahmen = frame wird erstellt
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=12)
frame.pack(fill=BOTH,expand=1)
 
# Einheitliche Hoehe für die Bilder 
baseheight = 450
 
# Bild aus dem gleichen Verzeichnis, wie dieses Python Programm
im = Image.open('blume.jpg')
width, height = im.size
 
# Bildgroesse anpassen
wpercent = baseheight/height
newwidth = width * wpercent
newwidth = int(newwidth)
newsize = (newwidth, baseheight) # Groesse als tuple
imnew = im.resize(newsize, PIL.Image.ANTIALIAS)
 
# Leinwand = Canvas definieren, auf der das Bild im Frame erscheint
canvas = Canvas(frame, width=newwidth, height=baseheight)
canvas.pack()
 
# Bild mit neuen Maßen wird mit der Leinwand = Canvas verbunden
canvas.image = ImageTk.PhotoImage(imnew)
 
# Bild wird angezeigt
canvas.create_image(0, 0, image=canvas.image, anchor='nw')
 
# Beschriftung unter dem Bild, im gleichen Rahmen
labela = tkinter.Label(frame, text="Original Bildbreite: %s px" % width, anchor='w')
labela.pack(fill=X, expand=1)
labelb = tkinter.Label(frame, text="Original Bildhoehe: %s px" % height, anchor='w')
labelb.pack(fill=X, expand=1)
 
# Exit Button
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=TOP)
 
tk.mainloop()

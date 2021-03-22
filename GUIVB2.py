from tkinter import *

gui = Tk(className='Python Examples - Window Size')
# set window size
gui.geometry("500x200")

#greeting = Label(text="Hello, Tkinter")
var=StringVar()
greeting=Label(gui, textvariable=var, relief=RAISED )
greeting2=Label(gui, textvariable=var, relief=RIDGE )

var.set("Hey!? How are you doing?")
greeting.pack()
greeting2.pack()

gui.mainloop() 
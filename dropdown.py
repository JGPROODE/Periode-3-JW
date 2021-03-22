#Import module 
from tkinter import *
  
# Create object 
root = Tk() 
  
# Adjust size 
root.geometry( "300x400" ) 
tekst=StringVar
# Change the label text 
#wordt iedere clik uitgevoerd
def show(): 
    label.config( text = clicked.get() )
    print("het label is: "+clicked.get())
    #tekst=text
    #dit werkt niet
  
# Dropdown menu options 
options = [ 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Monday" ) 
print("het label1 is: "+str(clicked.get()))
# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
# Create button, it will change label text 
button = Button( root , text = "click Me" , command = show ).pack() 
  
# Create Label 
label = Label( root , text = "hier is het label ") 





label.pack() 
print("het label is: "+str(clicked.get()))
  
# Execute tkinter 
root.mainloop() 
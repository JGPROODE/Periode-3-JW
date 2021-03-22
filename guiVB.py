import tkinter as tk
window = tk.Tk(className='Python Voorbeeld - Window Size')
window.geometry("300x500")
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()


window.mainloop()
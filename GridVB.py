import tkinter as tk

root = tk.Tk()
for r in range(12):
   for c in range(8):
      tk.Label(root, text='R%s/C%s'%(r,c),
         borderwidth=2 ).grid(row=r,column=c)
root.mainloop(  )
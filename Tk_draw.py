from tkinter import *
from tkinter import messagebox
root=Tk()

canvas=Canvas(root,height=500,width=500)
canvas.pack()

newline=canvas.create_line(100,300,20,100)




root.mainloop()
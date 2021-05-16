from tkinter import *
root=Tk()
Label(root,text="Hello Akhil").pack()

frame1=Frame(root)
frame1.pack()
#passing frame 1 here
btn=Button(frame1,text="OK",fg="white",bg="black")
btn.pack()

root.mainloop()
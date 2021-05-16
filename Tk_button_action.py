from tkinter import *
root=Tk()

def fun():
    print("Hello Button worked")

btn1=Button(root,text=" OK ",command=fun)
btn1.pack()


root.mainloop()
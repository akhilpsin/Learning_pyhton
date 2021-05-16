from tkinter import *
class fun:
    def __init__(self,root):
        self.b1l = Label(root, text="Button 1")
        self.b2l = Label(root, text="Button 2")
        self.b3l = Label(root, text="Button 3")

        self.btn1 = Button(root, text="Click",command=self.click)
        self.btn2 = Button(root, text="Cancel",command=self.cancel)
        self.btn3 = Button(root, text="Quit",command=root.quit)

        self.b1l.grid(row=0, column=0)
        self.b2l.grid(row=0, column=1)
        self.b3l.grid(row=0, column=2)
        self.btn1.grid(row=1, column=0)
        self.btn2.grid(row=1, column=1)
        self.btn3.grid(row=1, column=2)
    def click(self):
        print("Clicked Sucessfull")
    def cancel(self):
        print("Cancel Sucessfull")
root=Tk()
obj=fun(root)
root.mainloop()
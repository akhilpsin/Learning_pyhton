from tkinter import *
from tkinter import messagebox
root=Tk()

def np():
    print('Clickd New project')
def n():
    print('Clickd New ')
def ns():
    print('Clickd New scrach file ')
def op():
    print('Clickd Open ')
def sa():
    print('Clickd Save as ')

def udo():
    print('Clickd undo')
def cut():
    print('Clickd cut ')
def copy():
    print('Clickd copy ')
def copy_path():
    print('Clickd copy path ')
def paste():
    print('Clickd paste ')
def delete():
    print('Clickd paste ')

def t():
    print('Clickd tool')
def app():
    print('Clickd appearance ')
def qd():
    print('Clickd quick definition ')
def qtd():
    print('Clickd quick type definition ')
def qd():
    print('Clickd quick documentation ')
def pi():
    print('Clickd parameter info ')

def b():
    print('Clickd Back')
def cl():
    print('Clickd class ')
def fl():
    print('Clickd file ')
def sm():
    print('Clickd symbol ')
def lni():
    print('Clickd line ')
def nhe():
    print('Clickd next heighlight error ')

def g():
    print('Clickd Generate')
def cc():
    print('Clickd Code compilation ')
def ins():
    print('Clickd insert ')
def surr():
    print('Clickd surround with ')
def uw():
    print('Clickd un wrap ')
def f():
    print('Clickd folding ')

root_menu=Menu(root)
root.config(menu=root_menu)

menu1=Menu(root_menu)
root_menu.add_cascade(label='File',menu=menu1)
menu1.add_command(label='New project',command=np)
menu1.add_command(label='New',command=n)
menu1.add_separator()
menu1.add_command(label='New scrach file',command=ns)
menu1.add_command(label='Open',command=op)
menu1.add_separator()
menu1.add_command(label='Save as',command=sa)
menu1.add_command(label='Exit..',command=quit)


menu2=Menu(root_menu)
root_menu.add_cascade(label='Edit',menu=menu2)
menu2.add_command(label='undo',command=udo)
menu2.add_command(label='cut',command=cut)
menu2.add_separator()
menu2.add_command(label='copy',command=copy)
menu2.add_command(label='copy path',command=copy_path)
menu2.add_separator()
menu2.add_command(label='paste',command=paste)
menu2.add_command(label='delete',command=delete)


menu3=Menu(root_menu)
root_menu.add_cascade(label='View',menu=menu3)
menu3.add_command(label='tool',command=t)
menu3.add_command(label='appearance',command=app)
menu3.add_separator()
menu3.add_command(label='quick definition',command=qd)
menu3.add_command(label='quick type definition',command=qtd)
menu3.add_separator()
menu3.add_command(label='quick documentation',command=qd)
menu3.add_command(label='parameter info',command=pi)



menu4=Menu(root_menu)
root_menu.add_cascade(label='Navigate',menu=menu4)
menu4.add_command(label='back',command=b)
menu4.add_command(label='class',command=cl)
menu4.add_separator()
menu4.add_command(label='file',command=fl)
menu4.add_command(label='symbole',command=sm)
menu4.add_separator()
menu4.add_command(label='line',command=lni)
menu4.add_command(label='next heighlight error',command=nhe)


menu5=Menu(root_menu)
root_menu.add_cascade(label='Code',menu=menu5)
menu5.add_command(label='Generate',command=g)
menu5.add_command(label='Code compilation',command=cc)
menu5.add_separator()
menu5.add_command(label='Insert',command=ins)
menu5.add_command(label='Surround with',command=surr)
menu5.add_separator()
menu5.add_command(label='un wrap',command=uw)
menu5.add_command(label='folding',command=f)

toolbar=Frame(root,bg='light blue')
btn=Button(toolbar,text='crop')
btn.pack(side=LEFT,padx=3,pady=3)
toolbar.pack(side=TOP,fill=X)

statbar=Label(root,text=' This is status bar',relief=SUNKEN,bd=1,anchor=W)
statbar.pack(side=BOTTOM,fill=X)

root.mainloop()



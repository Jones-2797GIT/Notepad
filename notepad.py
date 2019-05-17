from tkinter import *
from tkinter import filedialog
import os

filename=""

def newFile():
    global filename
    filename=None
    root.title("Untitled - Notepad")
    entry.delete(1.0,END)

def openFile():
    global filename
    filename=filedialog.askopenfilename(defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if filename == "":
        filename=None
    else:
        root.title(os.path.basename(filename)+"- Notepad")
        entry.delete(1.0,END)
        f=open(filename,"r")
        entry.insert(1.0,f.read())
        f.close()


def saveFile():
    global filename
    if filename=="":
        filename=filedialog.asksaveasfilename(initialfile="Untitled - Notepad",defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if filename=="":
            filename=None
        else:
            f=open(filename,"w")
            f.write(entry.get(1.0,END))
            f.close()
            root.title(os.path.basename(filename)+" - Notepad ")
            print("File Saved")
    else:
        f = open(filename, "W")
        f.write(entry.get(1.0, END))
        f.close()


def cut():
    entry.event_generate(("<<Cut>>"))

def copy():
    entry.event_generate(("<<Copy>>"))

def paste():
    entry.event_generate(("<<Paste>>"))

def f():
    pass



root=Tk()
root.title("Untitled - Notepad")
root.iconbitmap(default="others\\images.jpg")
root.geometry('1000x500')



s1=Scrollbar(root, orient=VERTICAL)
s1.pack(side=RIGHT,fill=Y)

s2=Scrollbar(root, orient=HORIZONTAL)
s2.pack(side=BOTTOM,fill=X)

entry=Text(root)
entry=Text(root)
entry.pack(fill=BOTH,expand=True)


s1.config(command=entry.yview)
s2.config(command=entry.xview)
entry.config(yscrollcommand=s1.set,xscrollcommand=s2.set)




menu=Menu(root)
root.config(menu=menu)

filemenu=Menu(menu,tearoff=0)
filemenu.add_command(label="New         Ctrl+N",command=newFile)
filemenu.add_command(label="Open...     Ctrl+O",command=openFile)
filemenu.add_command(label="Save          Ctrl+S",command=saveFile)
filemenu.add_command(label="Save As...",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
menu.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menu,tearoff=0)
editmenu.add_command(label="Undo            Ctrl+Z",command=f)
editmenu.add_separator()
editmenu.add_command(label="Cut             Ctrl+X",command=cut)
editmenu.add_command(label="Copy            Ctrl+C",command=copy)
editmenu.add_command(label="Paste           Ctrl+V",command=paste)
editmenu.add_command(label="Delete          Del",command=f)
editmenu.add_separator()
editmenu.add_command(label="Find...               Ctrl+F",command=f)
editmenu.add_command(label="Find Next          F3",command=f)
editmenu.add_command(label="Replace...        Ctrl+H",command=f)
editmenu.add_command(label="Go To...           Ctrl+G",command=f)
editmenu.add_separator()
editmenu.add_command(label="Select All         Ctrl+A",command=f)
editmenu.add_command(label="Time/Date       F5",command=f)
menu.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menu,tearoff=0)
helpmenu.add_command(label="View Help",command=f)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad",command=f)
menu.add_cascade(label="Help",menu=helpmenu)



root.mainloop()
import sys
import tkinter
from tkinter import *

def close_window():
    window.destroy()
    sys.exit()

def freeze_window():
    root.attributes("-disabled", 1)

def free_window():
    root.attributes("-disabled", 0)

root= Tk()
root.title("主窗口")
root.geometry("500x500")
close = tkinter.Button(root,text="关闭",command=lambda :close_window()).place(x=50,y=50,width=100,height=50)
root.attributes("-disabled", 1)
window = Toplevel(root)  #生成子窗口，可以加入到事件中触发
window.title("子窗口")
window.geometry("300x300")
window.attributes("-topmost", 1)
freeze = tkinter.Button(window,text="冻结",command=lambda :freeze_window()).place(x=50,y=50,width=100,height=50)
free = tkinter.Button(window,text="解除",command=lambda :free_window()).place(x=150,y=50,width=100,height=50)
window.mainloop()
root.mainloop()


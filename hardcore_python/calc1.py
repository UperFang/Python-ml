from tkinter import *


root = Tk()#创建1个根窗口


#1.创建组件，创建组件的时候一定要指定容器
op1 = Entry(root)
op2 = Entry(root)

#2.需要把组件显示出来：grid、pack
# op1.pack(fill = BOTH)
op1.grid(row = 0, column = 0)
op2.grid(row = 0, column = 1)


root.geometry('500x500+100+100')


mainloop()

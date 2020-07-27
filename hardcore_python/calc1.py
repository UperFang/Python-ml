from tkinter import *
import re

#验证输入是否合法

def validate_iput():
    re.match()


def cmd_add():
   try:
        op1_value = float(op1.get())
        op2_value = float(op2.get())
        res = op1_value+op2_value
        res_var.set(res)
   except:
       res_var.set('请输入正确的操作数')
    

root = Tk()#创建1个根窗口


#1.创建组件，创建组件的时候一定要指定容器
#两个操作数
op1 = Entry(root)
op2 = Entry(root)

#操作按钮
btn_add = Button(root, text = '+', padx = 50, pady = 10, command = cmd_add)
btn_sub = Button(root, text = '-', padx = 50, pady = 10)
btn_mul = Button(root, text = '*', padx = 50, pady = 10)
btn_div = Button(root, text = '/', padx = 50, pady = 10)  
btn_mod = Button(root, text = '%', padx = 50, pady = 10)  
btn_flo = Button(root, text = '//', padx = 50, pady = 10)  
btn_exp = Button(root, text = '**', padx = 50, pady = 10)  
btn_clr = Button(root, text = 'clear', padx = 50, pady = 10)

res_var = StringVar()
res_var.set("Show Result")
result = Label(root, textvariable = res_var, pady = 50)  

#2.需要把组件显示出来：grid、pack
# # op1.pack(fill = BOTH)
op1.grid(row = 0, column = 0, columnspan = 4, sticky = 'WE')
op2.grid(row = 1, column = 0, columnspan = 4, sticky = 'WE')

btn_add.grid(row = 2, column = 0, sticky = 'WE')
btn_sub.grid(row = 2, column = 1, sticky = 'WE')
btn_mul.grid(row = 2, column = 2, sticky = 'WE')
btn_div.grid(row = 2, column = 3, sticky = 'WE')
btn_mod.grid(row = 3, column = 0, sticky = 'WE')
btn_flo.grid(row = 3, column = 1, sticky = 'WE')
btn_exp.grid(row = 3, column = 2, sticky = 'WE')
btn_clr.grid(row = 3, column = 3, sticky = 'WE')
result.grid(row = 4, column = 0, columnspan = 4, sticky = 'WE')

# root.geometry('500x500+100+100')


mainloop() 

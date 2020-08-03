from tkinter import *
import re

# 验证输入是否合法
# -229.12的规则：
# 1、+-开头或没有 [+-]?
# 2、大于1个的数字 [\d]+
# 3、可以有.或没有 [.]?
# 4、大于一个的数字 [\d]*
# '^&'头尾


def validate_iput():
    reg = '^[+-]?[\d]+[.]?[\d]*$'
    r1 = re.match(reg, op1.get())
    r2 = re.match(reg, op2.get())
    return r1 and r2

# 一、用异常捕捉处理
# def cmd_math():
#    try:
#         op1_value = float(op1.get())
#         op2_value = float(op2.get())
#         res = op1_value+op2_value
#         res_var.set(res)
#    except:
#        res_var.set('请输入正确的操作数')


# 二、利用正则表达式处理
def cmd_math(ops):
    is_valid = validate_iput()
    if is_valid:
        op1_value = float(op1.get())
        op2_value = float(op2.get())
        if (ops == '+'):
            res = op1_value + op2_value
        elif (ops == '-'):
            res = op1_value - op2_value
        elif (ops == '*'):
            res = op1_value * op2_value
        elif (ops == '/'):
            if(op2_value==0):
                res_var.set('除数不能为0')
            else:
                res = op1_value / op2_value
        elif (ops == '%'):
            res = op1_value % op2_value
        elif (ops == '//'):
            if(op2_value==0):
                res_var.set('除数不能为0')
            else:
                res = op1_value // op2_value
        elif (ops == '**'):
            res = op1_value ** op2_value 
        elif (ops == 'clear'):
            op1.delete(0,END) 
            op2.delete(0,END)
        res_var.set(round(res,2))
    else:
        res_var.set('请输入正确的操作数')

#使用eval计算表达式
def cal_exp():
    expression = op_expression.get()
    ans = eval(expression)#计算用户输入，存在安全隐患，因为eval还可以执行别的一系列命令
    res_var_exp.set(ans)
    pass


#创建根窗口和画布
root = Tk()  # 创建1个根窗口

menubar = Menu(root)#菜单和菜单里的内容都是用的Menu 
menu1 = Menu(menubar)
menu1.add_command(label='普通', command=lambda : f1.tkraise())#点了后托起f1画布
menu1.add_command(label='计算表达式', command=lambda : f2.tkraise())#点了后托起f1画布
menubar.add_cascade(label='模式',menu=menu1)
root.config(menu=menubar)


f1 = Frame(root)
f2 = Frame(root)
f1.grid(row = 0, column = 0, sticky = 'news')
f2.grid(row = 0, column = 0, sticky = 'news')

# 1.创建组件，创建组件的时候一定要指定容器
# 两个操作数
op1 = Entry(f1)
op2 = Entry(f1)

# 操作按钮
btn_add = Button(f1, text='+', padx=50, pady=10, command = lambda : cmd_math('+'))
btn_sub = Button(f1, text='-', padx=50, pady=10, command = lambda : cmd_math('-'))
btn_mul = Button(f1, text='*', padx=50, pady=10, command = lambda : cmd_math('*'))
btn_div = Button(f1, text='/', padx=50, pady=10, command = lambda : cmd_math('/'))
btn_mod = Button(f1, text='%', padx=50, pady=10, command = lambda : cmd_math('%'))
btn_flo = Button(f1, text='//', padx=50, pady=10, command = lambda : cmd_math('//'))
btn_exp = Button(f1, text='**', padx=50, pady=10, command = lambda : cmd_math('**'))
btn_clr = Button(f1, text='clear', padx=50, pady=10, command = lambda : cmd_math('clear'))

res_var = StringVar()
res_var.set("Show Result")
result = Label(f1, textvariable=res_var, pady=50)

# 2.需要把组件显示出来：grid、pack
# # op1.pack(fill = BOTH)
op1.grid(row=0, column=0, columnspan=4, sticky='WE')
op2.grid(row=1, column=0, columnspan=4, sticky='WE')

btn_add.grid(row=2, column=0, sticky='WE')
btn_sub.grid(row=2, column=1, sticky='WE')
btn_mul.grid(row=2, column=2, sticky='WE')
btn_div.grid(row=2, column=3, sticky='WE')
btn_mod.grid(row=3, column=0, sticky='WE')
btn_flo.grid(row=3, column=1, sticky='WE')
btn_exp.grid(row=3, column=2, sticky='WE')
btn_clr.grid(row=3, column=3, sticky='WE')
result.grid(row=4, column=0, columnspan=4, sticky='WE')

# root.geometry('500x500+100+100')

#布置f2画布内容
op_expression  = Entry(f2)
btn_cal = Button(f2, text = "计算", command = cal_exp)
res_var_exp = StringVar()
res_var_exp.set('计算结果：')
label_res = Label(f2,textvariable = res_var_exp)

op_expression.pack(fill = BOTH)
btn_cal.pack(fill = BOTH)
label_res.pack(fill = BOTH)

mainloop()

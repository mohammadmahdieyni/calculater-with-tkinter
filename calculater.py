from tkinter import *

tk = Tk()
tk.geometry("600x370")
tk.resizable(0, 0)
tk.title("Calculator")

def number(ad):
    global enter
    enter = enter + str(ad)
    env.set(enter)

def clear():
    en.delete(0)

def mosavi():
    global enter
    out = str(eval(enter))
    env.set(out)
    enter = ""


enter = ""
env = StringVar()
frame = Frame(tk, bg='light yellow')
frame.pack()
en = Entry(frame, textvariable=env, width=49, font=30, justify=RIGHT)
en.grid(row=1, column=2)
frame2 = Frame(tk, bg='light yellow')
frame2.pack()
btnd = Button(frame2, text='.', width=18, height=5, bg='light blue', command=lambda :number('.')).grid(row=2, column=0)
btn1 = Button(frame2, text='1', width=18, height=5,bg='light blue', command=lambda :number(1)).grid(row=2, column=1)
btn2 = Button(frame2, text='2', width=18, height=5,bg='light blue', command=lambda :number(2)).grid(row=2, column=2)
btn3 = Button(frame2, text='3', width=18, height=5,bg='light blue', command=lambda :number(3)).grid(row=2, column=3)
frame3 = Frame(tk, bg='light yellow')
frame3.pack()
btnt = Button(frame3, text='/', width=18, height=5,bg='light blue', command=lambda :number('/')).grid(row=2,column=0)
btn4 = Button(frame3, text='4', width=18, height=5,bg='light blue', command=lambda :number(4)).grid(row=2, column=1)
btn5 = Button(frame3, text='5', width=18, height=5,bg='light blue', command=lambda :number(5)).grid(row=2, column=2)
btn6 = Button(frame3, text='6', width=18, height=5,bg='light blue', command=lambda :number(6)).grid(row=2, column=3)
frame4 = Frame(tk)
frame4.pack()
btnz = Button(frame4, text='*', width=18, height=5,bg='light blue', command=lambda :number('*')).grid(row=2, column=0)
btn7 = Button(frame4, text='7', width=18, height=5,bg='light blue', command=lambda :number(7)).grid(row=2, column=1)
btn8 = Button(frame4, text='8', width=18, height=5,bg='light blue', command=lambda :number(8)).grid(row=2, column=2)
btn9 = Button(frame4, text='9', width=18, height=5,bg='light blue', command=lambda :number(9)).grid(row=2, column=3)

frame5 = Frame(tk)
frame5.pack()
btn0 = Button(frame5, text='0', width=18, height=5,bg='light blue', command=lambda :number(0)).grid(row=2, column=1)
btnm = Button(frame5, text='=', width=18, height=5,bg='light blue', command=mosavi).grid(row=2, column=2)
btnd = Button(frame5, text='+', width=18, height=5,bg='light blue', command=lambda :number('+')).grid(row=2, column=3)
cle = Button(frame5, text='clear', width=18, height=5,bg='black', fg='white', command=clear).grid(row=2, column=4)

tk.mainloop()
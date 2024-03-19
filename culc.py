import tkinter as tk


def add():
    num1 = int(num1_txt.get())
    num2 = int(num2_txt.get())
    result = num1 + num2
    res_txt.delete(0, "end")
    res_txt.insert(0, result)
    num1_txt.delete(0, "end")
    num2_txt.delete(0, "end")


def sub():
    num1 = int(num1_txt.get())
    num2 = int(num2_txt.get())
    result = num1 - num2
    res_txt.delete(0, "end")
    res_txt.insert(0, result)
    num1_txt.delete(0, "end")
    num2_txt.delete(0, "end")


def mul():
    num1 = int(num1_txt.get())
    num2 = int(num2_txt.get())
    result = num1 * num2
    res_txt.delete(0, "end")
    res_txt.insert(0, result)
    num1_txt.delete(0, "end")
    num2_txt.delete(0, "end")


def div():
    num1 = int(num1_txt.get())
    num2 = int(num2_txt.get())
    result = num1 / num2
    res_txt.delete(0, "end")
    res_txt.insert(0, result)
    num1_txt.delete(0, "end")
    num2_txt.delete(0, "end")


window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x500")
window.configure(bg="black")
window.resizable(False, False)
button_add = tk.Button(window, width=7, height=2, text='+', command=add,bg='silver')
button_add.place(x=150, y=250)
button_sub = tk.Button(window, width=7, height=2, text='-', command=sub,bg='silver')
button_sub.place(x=210, y=250)
button_mul = tk.Button(window, width=7, height=2, text='*', command=mul,bg='silver')
button_mul.place(x=150, y=350)
button_div = tk.Button(window, width=7, height=2, text='/', command=div,bg='silver')
button_div.place(x=210, y=350)
num1_txt = tk.Entry(window, width=30)
num1_txt.place(x=125, y=50)
num2_txt = tk.Entry(window, width=30)
num2_txt.place(x=125, y=100)
res_txt = tk.Entry(window,width=30)
res_txt.place(x=125, y=150)
window.mainloop()


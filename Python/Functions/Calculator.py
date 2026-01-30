from tkinter import *
import tkinter as tk
from Calcfunc.Addition import addition
from Calcfunc.Subtraction import subtraction
from Calcfunc.Multiplication import multiplication
from Calcfunc.Division import division
from Calcfunc.Percentage import percent
from Calcfunc.Indicies import Indicies
from Calcfunc.Root import root
from Calcfunc.Square import square
from Calcfunc.SqrRoot import sqrroot
from Calcfunc.Euler import euler
from Calcfunc.Pi import pi
from Calcfunc.Calc_Tree import Calculator_Tree



def Basic_calculator():
    application = Tk()
    application.geometry("400x700")
    application.title("Base_Calculator")
    application.config(bg="#000000")

    button_frame = Frame(application, bg="#000000")
    button_frame.pack(fill = 'both', expand =True, padx=10, pady=10,)

    entry_font = ("Segoe UI", 50)
    entry_a = Entry(application, font=entry_font, fg="#ccccdd", bg="#000044")
    entry_b = Entry(application, font=entry_font, fg="#ccccdd", bg="#000044")
    entry_symbol = Label(application, font=entry_font, fg="#ccccdd", bg="#000044")
    result_label = Label(application, font=entry_font, text="", fg="#aaaadd", bg="#000066")
    entry_a.place(x = 5, y = 10, width=163, height=75)
    entry_b.place(x = 272, y = 10, width=153, height=75)
    entry_symbol.place(x = 170, y = 10, width=100, height=75)
    result_label.place(x = 1, y = 100, width=420, height=75)

    input_target = 'a'
    current_operator = None

    def set_input_target(t):
        nonlocal input_target
        input_target = t
        entry_a.config(bg="#333366" if t != 'a' else "#555588")
        entry_b.config(bg="#333366" if t != 'b' else "#555588")

    def insert_digit(d):
        target = entry_a if input_target == 'a' else entry_b
        if d == '.':
            current = target.get()
            if '.' in current:
                return
            if current == '' or current == '-':
                target.insert(END, "0.")
            else:
                target.insert(END, '.')
            return         
        target.insert(END, str(d))
        
    def toggle_negative(e):
        target = entry_a if input_target == 'a' else entry_b
        if e == '-':
            current = target.get()
            if current.startswith('-'):
                target.delete(0,1)
            elif current != '':
                target.insert(0, '-')
            return
        target.insert(0, str(e))
        
    def Percent_operator(p):
        target = entry_a if input_target == 'a' else entry_b
        if p == '%':
            current = target.get()
            if current != '':
                res = percent(float(current)) #I GOT IT YAAAAAAAAAYAYYYYYYYYYYYYY
                target.delete(0, END)
                target.insert(0, res)
            return
        target.insert(text=str(res))
        
    def set_operator(op):
        nonlocal current_operator
        current_operator = op
        set_input_target('b')
        entry_symbol.config(text=op)
        
    def do_equal():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            if current_operator == '+':
                res = addition(a, b)
            elif current_operator == '-':
                res = subtraction(a, b)
            elif current_operator == '*':
                res = multiplication(a, b)
            elif current_operator == '/':
                res = division(a, b)
            else:
                result_label.config(text='no op')
                return
            result_label.config(text=str(round(res, 3)))
        except Exception:
            result_label.config(text='error')

    def empty():
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_symbol.config(text="")
        result_label.config(text="")
        set_input_target('a')

    entry_a.bind("<FocusIn>", lambda e: set_input_target('a'))
    entry_b.bind("<FocusIn>", lambda e: set_input_target('b'))

    button_font = ("Georgia")

    C = Button(button_frame, text='C', padx=60, pady=35, command=empty, fg="#00aa00", bg="#ffff00")
    Percent = Button(button_frame, text='%', padx=60, pady=35, command=lambda: Percent_operator('%'), fg="#00aa00", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
    Value0 = Button(button_frame, text = 0, padx=35, pady=35, command=lambda: insert_digit(0), fg="#000000", bg="#00cccc")
    Value1 = Button(button_frame, text = 1, padx=35, pady=35, command=lambda: insert_digit(1), fg="#ffffff", bg="#880000")
    Value2 = Button(button_frame, text = 2, padx=35, pady=35, command=lambda: insert_digit(2), fg="#ffffff", bg="#cc8800")
    Value3 = Button(button_frame, text = 3, padx=35, pady=35, command=lambda: insert_digit(3), fg="#ffffff", bg="#cccc00")
    Value4 = Button(button_frame, text = 4, padx=35, pady=35, command=lambda: insert_digit(4), fg="#ffffff", bg="#cccc00")
    Value5 = Button(button_frame, text = 5, padx=35, pady=35, command=lambda: insert_digit(5), fg="#ffffff", bg="#880000")
    Value6 = Button(button_frame, text = 6, padx=35, pady=35, command=lambda: insert_digit(6), fg="#ffffff", bg="#cc8800")
    Value7 = Button(button_frame, text = 7, padx=35, pady=35, command=lambda: insert_digit(7), fg="#ffffff", bg="#cc8800")
    Value8 = Button(button_frame, text = 8, padx=35, pady=35, command=lambda: insert_digit(8), fg="#ffffff", bg="#cccc00")
    Value9 = Button(button_frame, text = 9, padx=35, pady=35, command=lambda: insert_digit(9), fg="#ffffff", bg="#880000")
    Addition = Button(button_frame, text="+", padx=35, pady=35, command=lambda: set_operator('+'), fg="#cccccc", bg="#00aa00")
    Subtraction = Button(button_frame, text="-", padx=35, pady=35, command=lambda: set_operator('-'), fg="#cccccc", bg="#00aa00")
    Multiplication = Button(button_frame, text="*", padx=35, pady=35, command=lambda: set_operator('*'), fg="#cccccc", bg="#00aa00")
    Division = Button(button_frame, text="/", padx=35, pady=35, command=lambda: set_operator('/'), fg="#cccccc", bg="#00aa00")
    Equal = Button(button_frame, text="=", padx=35, pady=35, command=do_equal, fg="#ffffff", bg="#006600")
    Decimal = Button(button_frame, text=".", padx=35, pady=35, command=lambda: insert_digit('.'), fg="#ffffff", bg="#0066aa")
    Negative = Button(button_frame, text="+/-", padx=33, pady=33, command=lambda: toggle_negative('-'), fg="#ffffff", bg="#0066aa")

    C.place(x = 1, y = 200)
    Percent.place(x = 145, y = 200)
    Value0.place(x = 100, y = 600)
    Value1.place(x = 1, y = 500)
    Value2.place(x = 100, y = 500)
    Value3.place(x = 200, y =500)
    Value4.place(x = 1, y = 400)
    Value5.place(x = 100, y = 400)
    Value6.place(x = 200, y = 400)
    Value7.place(x = 1, y = 300)
    Value8.place(x = 100, y = 300)
    Value9.place(x = 200, y = 300)
    Addition.place(x = 300, y = 500)
    Subtraction.place(x = 300, y = 400)
    Multiplication.place(x = 300, y = 300)
    Division.place(x = 300, y = 200)
    Equal.place(x = 300, y = 600)
    Decimal.place(x = 200, y = 600)
    Negative.place(x = 1, y = 600)
    application.mainloop()
    
def Scientific_calculator():
    application = Tk()
    application.geometry("400x700")
    application.title("Science_Calculator")
    application.config(bg="black")

    button_frame = Frame(application, bg="#000033")
    button_frame.pack(fill = 'both', expand =True, padx=10, pady=10,)

    entry_font = ("Segoe UI", 50)
    entry_a = Entry(application, font=entry_font, fg="#ccccdd", bg="#333366")
    entry_b = Entry(application, font=entry_font, fg="#ccccdd", bg="#333366")
    entry_symbol = Label(application, font=entry_font, fg="#ccccdd", bg="#333366")
    result_label = Label(application, font=entry_font, text="", fg="#aaaadd", bg="#333399")
    entry_a.place(x = 5, y = 10, width=163, height=75)
    entry_b.place(x = 272, y = 10, width=153, height=75)
    entry_symbol.place(x = 170, y = 10, width=100, height=75)
    result_label.place(x = 15, y = 100, width=370, height=75)

    input_target = 'a'
    current_operator = None
    Last_ans = None

    def set_input_target(t):
        nonlocal input_target
        input_target = t
        entry_a.config(bg="#333366" if t != 'a' else "#555588")# Ich habe eine "Song Cover" gesehen aber ich kann es nicht findet.
        entry_b.config(bg="#333366" if t != 'b' else "#555588")#Ich werde diese Video pausieren. Ach vergiss es

    def insert_digit(d):
        target = entry_a if input_target == 'a' else entry_b
        if d == '.':
            current = target.get()
            if '.' in current:
                return
            if current == '' or current == '-':
                target.insert(END, "0.")
            else:
                target.insert(END, '.')
            return         
        target.insert(END, str(d))
        
    def toggle_negative(e):
        target = entry_a if input_target == 'a' else entry_b
        if e == '-':
            current = target.get()
            if current.startswith('-'):
                target.delete(0,1)
            elif current != '':
                target.insert(0, '-')
            return
        target.insert(0, str(e))
        
    def Percent_operator(p):
        target = entry_a if input_target == 'a' else entry_b
        if p == '%':
            current = target.get()
            if current != '':
                res = percent(float(current)) #I GOT IT YAAAAAAAAAYAYYYYYYYYYYYYY
                target.delete(0, END)
                target.insert(0, res)
            return
        target.insert(text=str(res))
        
        
    def set_operator(op):
        nonlocal current_operator
        current_operator = op
        set_input_target('b')
        entry_symbol.config(text=op)
        
    def do_equal():
        nonlocal Last_ans
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            if current_operator == '+':
                res = addition(a, b)
            elif current_operator == '-':
                res = subtraction(a, b)
            elif current_operator == '*':
                res = multiplication(a, b)
            elif current_operator == '/':
                res = division(a, b)
            else:
                result_label.config(text='no op')
                return
            Last_ans = round(res,3)
            result_label.config(text=str(round(res, 3)))
            
        except Exception:
            result_label.config(text='error')
            
    def ans():
        if Last_ans == None:
            return
        target = entry_a if input_target == 'a' else entry_b
        target.delete(0, END)
        target.insert(0, str(Last_ans))

    def empty():
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_symbol.config(text="")
        result_label.config(text="")
        set_input_target('a')

    entry_a.bind("<FocusIn>", lambda e: set_input_target('a'))
    entry_b.bind("<FocusIn>", lambda e: set_input_target('b'))

    C = Button(button_frame, text='C', padx=20, pady=20, command=empty, fg="#00aa00", bg="#ffff00")
    Percent = Button(button_frame, text='%', padx=20, pady=20, command=lambda: Percent_operator('%'), fg="#00aa00", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
    Value0 = Button(button_frame, text = 0, padx=20, pady=20, command=lambda: insert_digit(0), fg="#000000", bg="#00cccc")
    Value1 = Button(button_frame, text = 1, padx=20, pady=20, command=lambda: insert_digit(1), fg="#ffffff", bg="#880000")
    Value2 = Button(button_frame, text = 2, padx=20, pady=20, command=lambda: insert_digit(2), fg="#ffffff", bg="#cc8800")
    Value3 = Button(button_frame, text = 3, padx=20, pady=20, command=lambda: insert_digit(3), fg="#ffffff", bg="#cccc00")
    Value4 = Button(button_frame, text = 4, padx=20, pady=20, command=lambda: insert_digit(4), fg="#ffffff", bg="#cccc00")
    Value5 = Button(button_frame, text = 5, padx=20, pady=20, command=lambda: insert_digit(5), fg="#ffffff", bg="#880000")
    Value6 = Button(button_frame, text = 6, padx=20, pady=20, command=lambda: insert_digit(6), fg="#ffffff", bg="#cc8800")
    Value7 = Button(button_frame, text = 7, padx=20, pady=20, command=lambda: insert_digit(7), fg="#ffffff", bg="#cc8800")
    Value8 = Button(button_frame, text = 8, padx=20, pady=20, command=lambda: insert_digit(8), fg="#ffffff", bg="#cccc00")
    Value9 = Button(button_frame, text = 9, padx=20, pady=20, command=lambda: insert_digit(9), fg="#ffffff", bg="#880000")
    ValuePi = Button(button_frame, text = 'π', padx= 20, pady=20, fg="#ffffff", bg="#aa0000")
    ValueEu = Button(button_frame, text = "eˣ", padx=20, pady=20, fg="#ffffff", bg="#aa0000")
    ValueAns = Button(button_frame, text = "ans", padx=18, pady=18, command=ans, fg="#ffffff", bg="#00aa00")
    Sin = Button(button_frame, text="sin", padx=25, pady=20, fg="#aaaaaa", bg="#666666")
    Cos = Button(button_frame, text="cos", padx=25, pady=20, fg="#aaaaaa", bg="#666666")
    Tan = Button(button_frame, text="tan", padx=23, pady=20, fg="#aaaaaa", bg="#666666")
    Addition = Button(button_frame, text="+", padx=20, pady=20, command=lambda: set_operator('+'), fg="#cccccc", bg="#00aa00")
    Subtraction = Button(button_frame, text="-", padx=20, pady=20, command=lambda: set_operator('-'), fg="#cccccc", bg="#00aa00")
    Multiplication = Button(button_frame, text="*", padx=20, pady=20, command=lambda: set_operator('*'), fg="#cccccc", bg="#00aa00")
    Division = Button(button_frame, text="/", padx=20, pady=20, command=lambda: set_operator('/'), fg="#cccccc", bg="#00aa00")
    Equal = Button(button_frame, text="=", padx=18, pady=18, command=do_equal, fg="#ffffff", bg="#006600")
    Decimal = Button(button_frame, text=".", padx=20, pady=18, command=lambda: insert_digit('.'), fg="#ffffff", bg="#0066aa")
    Negative = Button(button_frame, text="+/-", padx=15, pady=17, command=lambda: toggle_negative('-'), fg="#ffffff", bg="#0066aa")
    Square = Button(button_frame, text = "x²", padx=19, pady=19, fg="#ffffff", bg="#0000ff")
    Power = Button(button_frame, text = "yˣ", padx=20, pady=20, fg="#00aa00", bg="#ffff00")
    SqrRoot = Button(button_frame, text = '√ ', padx=19, pady=19, fg="#ffffff", bg="#0000ff")
    Left = Button(button_frame, text = "←", padx=20, pady=19, fg="#ffffff", bg="#00bb00")
    Right = Button(button_frame, text = "→", padx=19, pady=18, fg="#ffffff", bg="#00bb00")
    Root = Button(button_frame, text = "ˣ√y", padx=17, pady=19, fg="#00aa00", bg="#ffff00")
    Brk1 = Button(button_frame, text = "(", padx=21, pady=20, fg ="#ffffff", bg="#00cc00")
    Brk2 = Button(button_frame, text = ")", padx=23, pady=20, fg="#ffffff", bg="#00cc00")

    C.place(x = 330, y = 420)
    Percent.place(x = 280, y = 420)
    Value0.place(x = 115, y = 610)
    Value1.place(x = 115, y = 550)
    Value2.place(x = 170, y = 550)
    Value3.place(x = 225, y = 550)
    Value4.place(x = 115, y = 485)
    Value5.place(x = 170, y = 485)
    Value6.place(x = 225, y = 485)
    Value7.place(x = 115, y = 420)
    Value8.place(x = 170, y = 420)
    Value9.place(x = 225, y = 420)
    ValuePi.place(x = 1, y = 420)
    ValueAns.place(x = 280, y = 610)
    ValueEu.place(x = 60, y = 420)
    Sin.place(x = 1, y = 355)
    Cos.place(x = 75, y = 355)
    Tan.place(x = 152, y = 355)
    Brk1.place(x = 225, y = 355)
    Brk2.place(x = 280, y = 355)
    Addition.place(x = 280, y = 485)
    Subtraction.place(x = 330, y = 485)
    Multiplication.place(x = 280, y = 550)
    Division.place(x = 330, y = 550)
    Equal.place(x = 330, y = 610)
    Decimal.place(x = 227, y = 615)
    Negative.place(x = 170, y = 615)
    Square.place(x = 60, y = 485)
    Power.place(x = 60, y = 550)
    SqrRoot.place(x = 1, y = 485)
    Root.place(x = 1, y = 550)
    Left.place(x = 1, y = 612)
    Right.place(x = 60, y = 615)
    application.mainloop()
    
def Currency_calculator():
    top = Tk()
    top.geometry("600x300")
    top.config(bg = "#888888")

    Font = ("Segoe UI", 15)

    label = Label(top, text = " Currencies", bg = "#cccccc")

    label.pack(pady = 10)

    List_frame = Frame(top, bg = "#cccccc")
    List_frame.pack(pady = 20)
    Button_frame = Frame(top, bg = "#cccccc")
    Button_frame.pack(pady = 20)


    Col1 = Frame(List_frame, bg = "#cccccc")
    Col1.pack(side = LEFT, padx = 30)

    Conv = Button(Button_frame, text="Convert", width = 10, height = 2)
    Conv.pack()


    label1 = Label(Col1, text = "FromCurr", bg = "#555555", fg = "#aaaaaa", width = 21)
    label1.pack()

    listbox1 = Listbox(Col1, width = 25, height = 3, font=Font)
    listbox1.pack()


    Col2 = Frame(List_frame, bg = "#333333")
    Col2.pack(side = LEFT, padx = 30)

    label2 = Label(Col2, text = "Tocurr", bg = "#555555", fg = "#aaaaaa", width = 21)
    label2.pack()

    listbox2 = Listbox(Col2, width = 25, height = 3, font=Font)
    listbox2.pack()

    Currencies = ["US Dollar", "EUR Euro", "GBR Pound", "CHR Frank", "JPY Yen", "CNY Yuan", "SEK Swedish Krona", "NOK Norwegian Krone", \
        "DKK Danish Krone", "RUB Ruble", "BWP Pula"]

    for Currency in Currencies:
        listbox1.insert(END, Currency)
        listbox2.insert(END, Currency)

    top.mainloop()
        
Set_up = Tk()
Set_up.geometry("400x600")
Set_up.title("Calculators")
Set_up.config(bg="black")

buttom_frame = Frame(Set_up, bg="black")
buttom_frame.pack(fill = 'both', expand=True)

Basic = Button(buttom_frame, text="Basic Calculator", command=Basic_calculator, padx=60, pady=20, fg = "#333366", bg = "#ccccff")
Scientific = Button(buttom_frame, text="Scientific Calculator", command=Scientific_calculator, padx=60, pady=20, fg = "#333366", bg = "#ccccff")
Currency = Button(buttom_frame, text="Currency Calculator", command=Currency_calculator, padx=60, pady=20, fg="#333366", bg="#ccccff")



Basic.place(x = 100, y = 100)
Scientific.place(x = 85, y = 200)
Currency.place(x = 90, y = 300)

Set_up.mainloop()
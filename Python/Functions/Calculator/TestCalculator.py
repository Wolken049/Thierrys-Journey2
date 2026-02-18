from tkinter import *
import tkinter as tk
from Calc_Tree import Calculator_Tree
import Calcfunc as Calc
    
def Scientific_calculator():
    global Calc
    
    application = tk.Tk()
    application.geometry("400x700")
    application.title("Science_Calculator")
    application.config(bg="black")

    button_frame = Frame(application, bg="#000033")
    button_frame.pack(fill = 'both', expand =True, padx=10, pady=10,)

    entry_font = ("Segoe UI", 50)
    
    def click(button_value):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current + str(button_value))
        
    def Percent_operator(p):
        target = "" #do later 
        if p == '%':
            current = target.get()
            if current != '':
                res = Calc.percent(float(current)) #I GOT IT YAAAAAAAAAYAYYYYYYYYYYYYY
                target.delete(0, END)
                target.insert(0, res)
            return
        target.insert(text=str(res))
    
    current_operator = None
    Last_ans = None

    display = tk.Entry(application, font = entry_font, relief = "ridge", justify = "right", fg = "#ffffff", bg = "#000066")
    display.pack(fill="both", padx = 10, pady = 0, ipady = 0)
            
    def ans():
        pass

    def empty():
        display.delete(0, tk.END)
        
    def do_equal():
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, result)
        except Exception:
            display.delete(0, END)
            display.insert(0, "Error")

    C = Button(button_frame, text='C', padx=20, pady=20, command=empty, fg="#00aa00", bg="#ffff00")
    Percent = Button(button_frame, text='%', padx=20, pady=20, command=lambda: Percent_operator('%'), fg="#00aa00", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
    Value0 = Button(button_frame, text = 0, padx=20, pady=20, command=lambda: click(0), fg="#000000", bg="#00cccc")
    Value1 = Button(button_frame, text = 1, padx=20, pady=20, command=lambda: click(1), fg="#ffffff", bg="#880000")
    Value2 = Button(button_frame, text = 2, padx=20, pady=20, command=lambda: click(2), fg="#ffffff", bg="#cc8800")
    Value3 = Button(button_frame, text = 3, padx=20, pady=20, command=lambda: click(3), fg="#ffffff", bg="#cccc00")
    Value4 = Button(button_frame, text = 4, padx=20, pady=20, command=lambda: click(4), fg="#ffffff", bg="#cccc00")
    Value5 = Button(button_frame, text = 5, padx=20, pady=20, command=lambda: click(5), fg="#ffffff", bg="#880000")
    Value6 = Button(button_frame, text = 6, padx=20, pady=20, command=lambda: click(6), fg="#ffffff", bg="#cc8800")
    Value7 = Button(button_frame, text = 7, padx=20, pady=20, command=lambda: click(7), fg="#ffffff", bg="#cc8800")
    Value8 = Button(button_frame, text = 8, padx=20, pady=20, command=lambda: click(8), fg="#ffffff", bg="#cccc00")
    Value9 = Button(button_frame, text = 9, padx=20, pady=20, command=lambda: click(9), fg="#ffffff", bg="#880000")
    ValuePi = Button(button_frame, text = 'π', padx= 20, pady=20, fg="#ffffff", bg="#aa0000")
    ValueEu = Button(button_frame, text = "eˣ", padx=20, pady=20, fg="#ffffff", bg="#aa0000")
    ValueAns = Button(button_frame, text = "ans", padx=18, pady=18, command=ans, fg="#ffffff", bg="#00aa00")
    Sin = Button(button_frame, text="sin", padx=25, pady=20, fg="#aaaaaa", bg="#666666")
    Cos = Button(button_frame, text="cos", padx=25, pady=20, fg="#aaaaaa", bg="#666666")
    Tan = Button(button_frame, text="tan", padx=23, pady=20, fg="#aaaaaa", bg="#666666")
    Addition = Button(button_frame, text="+", padx=20, pady=20, command=lambda: click('+'), fg="#cccccc", bg="#00aa00")
    Subtraction = Button(button_frame, text="-", padx=20, pady=20, command=lambda: click('-'), fg="#cccccc", bg="#00aa00")
    Multiplication = Button(button_frame, text="*", padx=20, pady=20, command=lambda: click('*'), fg="#cccccc", bg="#00aa00")
    Division = Button(button_frame, text="/", padx=20, pady=20, command=lambda: click('/'), fg="#cccccc", bg="#00aa00")
    Equal = Button(button_frame, text="=", padx=18, pady=18, command=do_equal, fg="#ffffff", bg="#006600")
    Decimal = Button(button_frame, text=".", padx=20, pady=18, command=lambda: click('.'), fg="#ffffff", bg="#0066aa")
    Negative = Button(button_frame, text="+/-", padx=15, pady=17, command=lambda: toggle_negative('-'), fg="#ffffff", bg="#0066aa")
    Square = Button(button_frame, text = "x²", padx=19, pady=19, fg="#ffffff", bg="#0000ff")
    Power = Button(button_frame, text = "yˣ", padx=20, pady=20, fg="#00aa00", bg="#ffff00")
    SqrRoot = Button(button_frame, text = '√ ', padx=19, pady=19, fg="#ffffff", bg="#0000ff")
    Left = Button(button_frame, text = "←", padx=20, pady=19, fg="#ffffff", bg="#00bb00")
    Right = Button(button_frame, text = "→", padx=19, pady=18, fg="#ffffff", bg="#00bb00")
    Root = Button(button_frame, text = "ˣ√y", padx=17, pady=19, fg="#00aa00", bg="#ffff00")
    Brk1 = Button(button_frame, text = "(", command = lambda: click('('), padx=21, pady=20, fg ="#ffffff", bg="#00cc00")
    Brk2 = Button(button_frame, text = ")", command = lambda: click(')'), padx=23, pady=20, fg="#ffffff", bg="#00cc00")

    C.place(x = 330, y = 420)
    Percent.place(x = 280, y = 420)
    Value0.place(x = 170, y = 610)
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
    Negative.place(x = 115, y = 615)
    Square.place(x = 60, y = 485)
    Power.place(x = 60, y = 550)
    SqrRoot.place(x = 1, y = 485)
    Root.place(x = 1, y = 550)
    Left.place(x = 1, y = 612)
    Right.place(x = 60, y = 615)
    application.mainloop()
    
        
Set_up = Tk()
Set_up.geometry("400x600")
Set_up.title("Calculators")
Set_up.config(bg="black")

buttom_frame = Frame(Set_up, bg="black")
buttom_frame.pack(fill = 'both', expand=True)

Scientific = Button(buttom_frame, text="Scientific Calculator", command=Scientific_calculator, padx=60, pady=20, fg = "#333366", bg = "#ccccff")



Scientific.place(x = 85, y = 200)

Set_up.mainloop()
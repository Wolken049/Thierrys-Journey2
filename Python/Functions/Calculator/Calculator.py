from tkinter import *
import tkinter as tk
from Calc_Tree import Calculator_Tree
import Calcfunc as Calc
import re

def Basic_calculator():
    global Calc
    
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
                res = Calc.percent(float(current)) #I GOT IT YAAAAAAAAAYAYYYYYYYYYYYYY
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
                res = Calc.add(a, b)
            elif current_operator == '-':
                res = Calc.sub(a, b)
            elif current_operator == '*':
                res = Calc.multi(a, b)
            elif current_operator == '/':
                res = Calc.div(a, b)
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
    global Calc
    Degrees = Calc.Trig.Trig1
    Radians = Calc.Trig.Trig2
    
    application = tk.Tk()
    application.geometry("450x700")
    application.title("Science_Calculator")
    application.config(bg="black")
    button_frame = Frame(application, bg="#000066",width = 30, height =30)
    button_frame.pack(fill = 'both', expand =True)
    
    colour = True
        
    entry_font = ("Segoe UI", 30)
    
    def click(button_value):
        nonlocal option, Trig_flag
        if not option:
            current = display1.get()
            display1.delete(0, tk.END)
            display1.insert(0, current + str(button_value))
        else:
            display1.delete(0, tk.END)
            if Trig_option:
                if button_value == 1:
                    Trig_flag = 1
                    display1.delete(0, tk.END)
                    option = False
                elif button_value == 2:
                    Trig_flag = 2
                    display1.delete(0, END)
                    option = False
                elif button_value == 3:
                    Trig_flag = 3
                    display1.delete(0, END)
                    option = False
            
        
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
    Trig_flag = 1
    InvTrig = False
    Trig_option = False
    CmdShift = False
    CmdAlpha = False
    option = False
    
    A = None
    B = None
    C = None
    D = None
    E = None
    F = None

    display1 = tk.Entry(application, font = entry_font, relief = "ridge", justify = "right", fg = "#ffffff", bg = "#000099")
    display1.pack(fill="both", padx = 5, pady = 5, ipady = 5)
    display1.place(x = 0, y = 5, width = 450, height = 60)
    
    display2 = tk.Entry(application, font = entry_font, relief = "ridge", justify = "right", fg = "#ffffff", bg = "#000099")
    display2.pack(fill="both", padx = 5, pady = 5, ipady = 5)
    display2.place(x = 0, y = 70, width = 450, height = 60)
    
    display3 = tk.Entry(application, font = ("Segoe UI", 7), relief = "ridge", justify = "center", fg = "#ffffff", bg = "#000099")
    display3.pack(fill="both", padx = 5, pady = 5, ipady = 5)
    display3.place(x = 212, y = 150, width = 30, height = 25)
    
    def ans():
        nonlocal Last_ans
        display1.delete(0, tk.END)
        display1.insert(0, Last_ans)
        
    def storage():
        nonlocal Last_ans, CmdAlpha, CmdShift
        CmdShift = False
        CmdAlpha = True
        
        
    def emptytop():
        display1.delete(0, tk.END)
        
    def emptyall():
        display1.delete(0, tk.END)
        display2.delete(0, tk.END)
    
    def delete():
        current = display1.get()
        display1.delete(0, END)
        display1.insert(0, current[:-1])
        
    def shift():
        nonlocal InvTrig, CmdShift, CmdAlpha
        CmdAlpha = False #Logic Error: Buttons don't reset when you immediately press Alpha button making shifted buttons stay shifted lest shift is pressed again
        if not InvTrig:
            InvTrig = True
            Sin.config(text="sin⁻¹", command=lambda: click("sin⁻¹("))
            Cos.config(text="cos⁻¹", command=lambda: click("cos⁻¹("))
            Tan.config(text="tan⁻¹", command=lambda: click("tan⁻¹("))
        else:
            InvTrig = False
            Sin.config(text="sin", command=lambda: click("sin("))
            Cos.config(text="cos", command=lambda: click("cos("))
            Tan.config(text="tan", command=lambda: click("tan("))
            
        if not CmdShift:
            CmdShift = True
            Inverse.config(text="x!", command=lambda: click('!'))
            Valueln.config(text = "eˣ", command=lambda: click("e("))
            Power.config(text = "ˣ√y")
            display3.delete(0, tk.END)
            display3.insert(0, "Shift")
            
        else:
            CmdShift = False        
            Inverse.config(text = "x⁻¹",command=lambda: click('⁻¹'))
            Valueln.config(text = "ln", command=lambda:click("ln("))
            Power.config(text = "yˣ")
            display3.delete(0, tk.END)
            
            

    def alpha():
        nonlocal CmdAlpha, CmdShift, InvTrig
        InvTrig = False
        CmdShift = False #Logic Error: Buttons don't reset when you immediately press Shift button making shifted buttons stay shifted lest shift is pressed again
        if not CmdAlpha:
            CmdAlpha = True
            time.config(text="B", command=lambda: click("B"))
            Hyp.config(text="C", command=lambda: click("C"))
            Sin.config(text="D", command=lambda: click("D"))
            Cos.config(text="E", command=lambda: click("E"))
            Tan.config(text="F", command=lambda: click("F"))
            Valueln.config(text = "ℯ", command=lambda: click("ℯ"))
            display3.delete(0, tk.END)
            display3.insert(0, "Alpha")
        else:
            CmdAlpha = False
            time.config(text="°")
            Hyp.config(text="hyp")
            Sin.config(text="sin", command=lambda: click("sin("))
            Cos.config(text="cos", command=lambda: click("cos("))
            Tan.config(text="tan", command=lambda: click("tan("))
            Valueln.config(text = "ln", command=lambda: click("ln("))
            display3.delete(0, tk.END)
    def colourchange():
        nonlocal colour
        if not colour:
            button_frame.config(bg = "#000066")
            display1.config(bg = "#000099")
            display2.config(bg = "#000099")
            display3.config(bg = "#000099")
            colour = True
            Clear.config(fg = "#ffffff", bg="#000000")
            ac.config(fg="#ffffff", bg="#aabb99")
            Delete.config(bg="#aabb99")
            Percent.config(fg="#00aa00", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
            Value0.config(fg="#ffffff", bg="#00cccc")
            Value1.config(fg="#ffffff", bg="#880000")
            Value2.config(fg="#ffffff", bg="#cc8800")
            Value3.config(fg="#ffffff", bg="#cccc00")
            Value4.config(fg="#ffffff", bg="#cccc00")
            Value5.config(fg="#ffffff", bg="#880000")
            Value6.config(fg="#ffffff", bg="#cc8800")
            Value7.config(fg="#ffffff", bg="#cc8800")
            Value8.config(fg="#ffffff", bg="#cccc00")
            Value9.config(fg="#ffffff", bg="#880000")
            ValuePi.config(fg="#ffffff", bg="#aa0000")
            Valueln.config(fg="#ffffff", bg="#0066aa")
            ValueAns.config(fg="#ffffff", bg="#00aa00")
            Sin.config(fg="#ffffff", bg="#aa0066")
            Cos.config(fg="#ffffff", bg="#aa0066")
            Tan.config(fg="#ffffff", bg="#aa0066")
            Hyp.config(fg="#aaaaaa", bg="#666666")
            time.config(fg="#aaaaaa", bg="#aa0066")
            log.config(fg="#ffffff", bg="#0066aa")
            A.config(fg="#ff8800", bg="#ffffff")
            B.config(fg="#ff8800", bg="#ffffff")
            C.config(fg="#ff8800", bg="#ffffff")
            D.config(fg="#ff8800", bg="#ffffff")
            E.config(fg="#ff8800", bg="#ffffff")
            F.config(fg="#ff8800", bg="#ffffff")
            X.config(fg="#ff8800", bg="#ffffff")
            Y.config(fg="#ff8800", bg="#ffffff")
            M.config(fg="#ffffff", bg="#00ddaa")
            Addition.config(fg="#cccccc", bg="#00aa00")
            Subtraction.config(fg="#cccccc", bg="#00aa00")
            Multiplication.config(fg="#cccccc", bg="#00aa00")
            Division.config(fg="#cccccc", bg="#00aa00")
            Equal.config(fg="#ffffff", bg="#006600")
            Decimal.config(fg="#ffffff", bg="#0066aa")
            Negative.config(fg="#ffffff", bg="#0066aa")
            Inverse.config(fg="#ffffff", bg="#aa9900")
            Square.config(fg="#ffffff", bg="#aa6600")
            Cube.config(fg="#ffffff", bg="#aa9900")
            Power.config(fg="#ffffff", bg="#aa6600")
            SqrRoot.config(fg="#ffffff", bg="#aa6600")
            Left.config(fg="#ffffff", bg="#00bb00")
            Right.config(fg="#ffffff", bg="#00bb00")
            Root.config(fg="#00aa00", bg="#ffff00")
            Brk1.config(fg ="#ffffff", bg="#00cc00")
            Brk2.config(width=9, height=3, fg="#ffffff", bg="#00cc00")
            Shift.config(fg="#ffffff", bg="#0099aa")
            Alpha.config(fg="#ffffff", bg="#0099aa")
            Trigo.config(fg="#ffffff", bg="#0099aa")
            Color.config(fg="#ffffff", bg="#0099aa")
            sto.config(fg="#ffffff", bg="#0033aa")
        else:
            colour = False
            button_frame.config(bg = "#000000")
            display1.config(bg = "#000000")
            display2.config(bg = "#000000")
            display3.config(bg = "#000000")
            Clear.config(fg = "#ffffff", bg="#000000")
            ac.config(fg="#ffffff", bg="#000000")
            Delete.config(fg="#ffffff", bg="#000000")
            Percent.config(fg="#ffffff", bg="#000000")#Ich bin ein Idiot oida, wie ich vergessen kann
            Value0.config(fg="#ffffff", bg="#000000")
            Value1.config(fg="#ffffff", bg="#000000")
            Value2.config(fg="#ffffff", bg="#000000")
            Value3.config(fg="#ffffff", bg="#000000")
            Value4.config(fg="#ffffff", bg="#000000")
            Value5.config(fg="#ffffff", bg="#000000")
            Value6.config(fg="#ffffff", bg="#000000")
            Value7.config(fg="#ffffff", bg="#000000")
            Value8.config(fg="#ffffff", bg="#000000")
            Value9.config(fg="#ffffff", bg="#000000")
            ValuePi.config(fg="#ffffff", bg="#000000")
            Valueln.config(fg="#ffffff", bg="#000000")
            ValueAns.config(fg="#ffffff", bg="#000000")
            Sin.config(fg="#ffffff", bg="#000000")
            Cos.config(fg="#ffffff", bg="#000000")
            Tan.config(fg="#ffffff", bg="#000000")
            Hyp.config(fg="#ffffff", bg="#000000")
            time.config(fg="#ffffff", bg="#000000")
            log.config(fg="#ffffff", bg="#000000")
            A.config(fg="#ffffff", bg="#000000")
            B.config(fg="#ffffff", bg="#000000")
            C.config(fg="#ffffff", bg="#000000")
            D.config(fg="#ffffff", bg="#000000")
            E.config(fg="#ffffff", bg="#000000")
            F.config(fg="#ffffff", bg="#000000")
            X.config(fg="#ffffff", bg="#000000")
            Y.config(fg="#ffffff", bg="#000000")
            M.config(fg="#ffffff", bg="#000000")
            Addition.config(fg="#ffffff", bg="#000000")
            Subtraction.config(fg="#ffffff", bg="#000000")
            Multiplication.config(fg="#ffffff", bg="#000000")
            Division.config(fg="#ffffff", bg="#000000")
            Equal.config(fg="#ffffff", bg="#000000")
            Decimal.config(fg="#ffffff", bg="#000000")
            Negative.config(fg="#ffffff", bg="#000000")
            Inverse.config(fg="#ffffff", bg="#000000")
            Square.config(fg="#ffffff", bg="#000000")
            Cube.config(fg="#ffffff", bg="#000000")
            Power.config(fg="#ffffff", bg="#000000")
            SqrRoot.config(fg="#ffffff", bg="#000000")
            Left.config(fg="#ffffff", bg="#000000")
            Right.config(fg="#ffffff", bg="#000000")
            Root.config(fg="#ffffff", bg="#000000")
            Brk1.config(fg ="#ffffff", bg="#000000")
            Brk2.config(fg="#ffffff", bg="#000000")
            Shift.config(fg="#ffffff", bg="#000000")
            Alpha.config(fg="#ffffff", bg="#000000")
            Trigo.config(fg="#ffffff", bg="#000000")
            Color.config(fg="#ffffff", bg="#000000")
            sto.config(fg="#ffffff", bg="#000000")
            
    def Trig():
        nonlocal option, Trig_option
        option = True
        Trig_option = True
        display1.delete(0, END)
        display1.insert(0, "Deg (1), Rad (2)")
                      
    def do_equal():
        nonlocal Last_ans, option
        expression = display1.get()
        
        print("RAW:", expression)
        
        if not option:
            try:
                expression = display1.get()
                expression = re.sub(r'(\d)(π)', r'\1*\2', expression)
                expression = re.sub(r'e\(([^)]+)\)', lambda m: f"{(Calc.euler(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'ln\(([^)]+)\)', lambda m: f"{(Calc.ln(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'log\(([^)]+)\)', lambda m: f"{(Calc.log(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'(\d+\.?\d*)!', lambda m: f"{(Calc.factorial(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'√(\d+\.?\d*)', lambda m: f"{(Calc.SqrRoot(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'\(([^)]+)\)%', lambda m: f"{(Calc.percent(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'(\d+\.?\d*)%', lambda m: f"{(Calc.percent(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'\(([^)]+)\)⁻¹', lambda m: f"{(Calc.Inverse(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'(\d+\.?\d*)⁻¹', lambda m: f"{(Calc.Inverse(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'\(([^)]+)\)²', lambda m: f"{(Calc.Square(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'(\d+\.?\d*)²', lambda m: f"{(Calc.Square(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'(\d+\.?\d*)\(', r'\1*(', expression)
                expression = re.sub(r'\(([^)]+)\)³', lambda m: f"{(Calc.Cube(eval(m.group(1)))):.10f}", expression)
                expression = re.sub(r'(\d+\.?\d*)³', lambda m: f"{(Calc.Cube(eval(m.group(1)))):.10f}", expression)
                expression = expression.replace("π", str(Calc.pi()))
                expression = expression.replace("ℯ", str(Calc.empeuler()))
                expression = re.sub(r'√\(([^)]+)\)', lambda m: f"{(Calc.SqrRoot(eval(m.group(1)))):.10f}", expression)
                expression = expression.replace("ans", str(Last_ans))
                
                match Trig_flag:
                    case 1:
                        if not InvTrig:
                            expression = re.sub(r'sin\(([^)]+)\)', lambda m: f"{(Degrees.degsine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'cos\(([^)]+)\)', lambda m: f"{(Degrees.degcosine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'tan\(([^)]+)\)', lambda m: f"{(Degrees.degtangent(eval(m.group(1)))):.10f}", expression)
                        else:
                            expression = re.sub(r'sin⁻¹\(([^)]+)\)', lambda m: f"{(Degrees.invdegsine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'cos⁻¹\(([^)]+)\)', lambda m: f"{(Degrees.invdegcosine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'tan⁻¹\(([^)]+)\)', lambda m: f"{(Degrees.invdegtangent(eval(m.group(1)))):.10f}", expression)
                    case 2:
                        if not InvTrig:
                            expression = re.sub(r'sin\(([^)]+)\)', lambda m: f"{(Radians.radsine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'cos\(([^)]+)\)', lambda m: f"{(Radians.radcosine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'tan\(([^)]+)\)', lambda m: f"{(Radians.radtangent(eval(m.group(1)))):.10}", expression)
                        else: 
                            expression = re.sub(r'sin⁻¹\(([^)]+)\)', lambda m: f"{(Radians.invradsine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'cos⁻¹\(([^)]+)\)', lambda m: f"{(Radians.invradcosine(eval(m.group(1)))):.10f}", expression)
                            expression = re.sub(r'tan⁻¹\(([^)]+)\)', lambda m: f"{(Radians.invradtangent(eval(m.group(1)))):.10}", expression)
                    case 3:
                        pass
                    case 4:
                        pass
                print(expression)
                result = eval(expression)#Why does the position of this matter? (Context: I moved this line up and it caused errors)
                Last_ans = result
                fresult = round(result, 9)
                display2.delete(0, tk.END)
                display2.insert(0, fresult)
            except Exception as e:
                print("Error: ", e)
                match e:
                    case ZeroDivisionError():
                        display2.delete(0, END)
                        display2.insert(0, "Math ERROR") #Wenn der Benutzer durch 0 dividiert, zeigt die Funktion "Math Error" zurück an
                    case ValueError():
                        display2.delete(0, END)
                        display2.insert(0, "Math ERROR")#Wenn der Benutzer 
                    case _:
                        display2.delete(0, END)
                        display2.insert(0, "Syntax ERROR")# Wenn der Benutzer eine Unvollständige oder ungültige Gleichung eingibt, zeigt die Funktion "Syntax Error" an  

    Clear = Button(button_frame, text='C', width=11, height=5, command=emptytop, fg="#00aa00", bg="#ffff00")
    ac = Button(button_frame, text='AC', width=11, height=5, command=emptyall, fg="#ffffff", bg="#99bbaa")
    Delete = Button(button_frame, text="Del", width=11, height=5, command=delete, fg="#ffffff", bg="#aabb99")
    Percent = Button(button_frame, text='%', width=9, height=3, command=lambda: click('%'), fg="#00aa00", bg="#ffff00")#Ich bin ein Idiot oida, wie ich vergessen kann
    Value0 = Button(button_frame, text = 0, width=11, height=5, command=lambda: click(0), fg="#000000", bg="#00cccc")
    Value1 = Button(button_frame, text = 1, width=11, height=5, command=lambda: click(1), fg="#ffffff", bg="#880000")
    Value2 = Button(button_frame, text = 2, width=11, height=5, command=lambda: click(2), fg="#ffffff", bg="#cc8800")
    Value3 = Button(button_frame, text = 3, width=11, height=5, command=lambda: click(3), fg="#ffffff", bg="#cccc00")
    Value4 = Button(button_frame, text = 4, width=11, height=5, command=lambda: click(4), fg="#ffffff", bg="#cccc00")
    Value5 = Button(button_frame, text = 5, width=11, height=5, command=lambda: click(5), fg="#ffffff", bg="#880000")
    Value6 = Button(button_frame, text = 6, width=11, height=5, command=lambda: click(6), fg="#ffffff", bg="#cc8800")
    Value7 = Button(button_frame, text = 7, width=11, height=5, command=lambda: click(7), fg="#ffffff", bg="#cc8800")
    Value8 = Button(button_frame, text = 8, width=11, height=5, command=lambda: click(8), fg="#ffffff", bg="#cccc00")
    Value9 = Button(button_frame, text = 9, width=11, height=5, command=lambda: click(9), fg="#ffffff", bg="#880000")
    ValuePi = Button(button_frame, text = 'π', width=9, height=3, command=lambda: click("π"), fg="#ffffff", bg="#aa0000")
    Valueln = Button(button_frame, text = "ln", command=lambda: click("ln"),width=9, height=3, fg="#ffffff", bg="#0066aa")
    ValueAns = Button(button_frame, text = "ans", width=11, height=5, command=lambda: click("ans"), fg="#ffffff", bg="#006600")
    Sin = Button(button_frame, text="sin", width=9, height=3, command=lambda: click("sin"), fg="#ffffff", bg="#aa0066")
    Cos = Button(button_frame, text="cos", width=9, height=3, command=lambda: click("cos"), fg="#ffffff", bg="#aa0066")
    Tan = Button(button_frame, text="tan", width=9, height=3, command=lambda: click("tan"), fg="#ffffff", bg="#aa0066")
    Hyp = Button(button_frame, text="hyp", width=9, height=3, fg="#aaaaaa", bg="#666666")
    time = Button(button_frame, text="°", width=9, height=3, fg="#aaaaaa", bg="#aa0066")
    log = Button(button_frame, text="log", width=9, height=3, command=lambda: click("log"),fg="#ffffff", bg="#0066aa")
    A = Button(button_frame, text = 'A', width=9, height=3, command=lambda: click(A), fg="#ff8800", bg="#ffffff")
    B = Button(button_frame, text = 'B', width=9, height=3, command=lambda: click(B), fg="#ff8800", bg="#ffffff")
    C = Button(button_frame, text = 'C', width=9, height=3, command=lambda: click(C), fg="#ff8800", bg="#ffffff")
    D = Button(button_frame, text = 'D', width=9, height=3, command=lambda: click(D), fg="#ff8800", bg="#ffffff")
    E = Button(button_frame, text = 'E', width=9, height=3, command=lambda: click(E), fg="#ff8800", bg="#ffffff")
    F = Button(button_frame, text = 'F', width=9, height=3, command=lambda: click(F), fg="#ff8800", bg="#ffffff")
    X = Button(button_frame, text = 'X', width=9, height=3, command=lambda: click(X), fg="#ff8800", bg="#ffffff")
    Y = Button(button_frame, text = 'Y', width=9, height=3, command=lambda: click(Y), fg="#ff8800", bg="#ffffff")
    M = Button(button_frame, text = 'Z', width=9, height=3, command=lambda: click(M), fg="#ff8800", bg="#ffffff")
    Addition = Button(button_frame, text="+", width=11, height=5, command=lambda: click('+'), fg="#cccccc", bg="#00aa00")
    Subtraction = Button(button_frame, text="-", width=11, height=5, command=lambda: click('-'), fg="#cccccc", bg="#00aa00")
    Multiplication = Button(button_frame, text="*", width=11, height=5, command=lambda: click('*'), fg="#cccccc", bg="#00aa00")
    Division = Button(button_frame, text="/", width=11, height=5, command=lambda: click('/'), fg="#cccccc", bg="#00aa00")
    Equal = Button(button_frame, text="=", width=11, height=5, command=do_equal, fg="#ffffff", bg="#006600")
    Decimal = Button(button_frame, text=".", width=11, height=5, command=lambda: click('.'), fg="#ffffff", bg="#0066aa")
    Negative = Button(button_frame, text="+/-", width=11, height=5, fg="#ffffff", bg="#0066aa")
    Inverse = Button(button_frame, text = "x⁻¹", width=9, height=3, command=lambda: click('⁻¹'), fg="#ffffff", bg="#aa9900")
    Square = Button(button_frame, text = "x²", width=9, height=3, command=lambda: click('²'), fg="#ffffff", bg="#aa6600")
    Cube = Button(button_frame, text = "x³", width=9, height=3, command=lambda: click('³'), fg="#ffffff", bg="#aa9900")
    Power = Button(button_frame, text = "yˣ", width=9, height=3, fg="#ffffff", bg="#aa6600")
    SqrRoot = Button(button_frame, text = '√ ', width=9, height=3, command=lambda: click('√'),fg="#ffffff", bg="#aa6600")
    Left = Button(button_frame, text = "←", width=3, height=1, fg="#ffffff", bg="#00bb00")
    Right = Button(button_frame, text = "→", width=3, height=1, fg="#ffffff", bg="#00bb00")
    Root = Button(button_frame, text = "ˣ√y", width=9, height=3, fg="#00aa00", bg="#ffff00")
    Brk1 = Button(button_frame, text = "(", command = lambda: click('('), width=9, height=3, fg ="#ffffff", bg="#00cc00")
    Brk2 = Button(button_frame, text = ")", command = lambda: click(')'), width=9, height=3, fg="#ffffff", bg="#00cc00")
    Shift = Button(button_frame, text="Shift", width=9, height=1, command=shift, fg="#ffffff", bg="#0099aa")
    Alpha = Button(button_frame, text="Alpha", width=9, height=1, command=alpha, fg="#ffffff", bg="#0099aa")
    Trigo = Button(button_frame, text="Trig", width=9, height=1, command=Trig, fg="#ffffff", bg="#0099aa")
    Color = Button(button_frame, text="Colour", command=colourchange,width=9, height=1, fg="#ffffff", bg="#0099aa")
    sto = Button(button_frame, text="sto", width=9, height=3, command=storage, fg="#ffffff", bg="#0033aa")
    M = Button(button_frame, text="M",width=9, height=3, fg="#ffffff", bg="#00ddaa")
    
        
    Shift.place(x = 0, y = 136)
    Alpha.place(x = 0, y = 163)
    Trigo.place(x = 300, y = 136)
    Color.place(x = 300, y = 163)
    #Clear.place(x = 360, y = 360)
    ac.place(x = 360, y = 360)
    Delete.place(x = 270, y = 360)
    Percent.place(x = 75, y = 304)
    Value0.place(x = 90, y = 615)
    Value1.place(x = 0, y = 530)
    Value2.place(x = 90, y = 530)
    Value3.place(x = 180, y = 530)
    Value4.place(x = 0, y = 445)
    Value5.place(x = 90, y = 445)
    Value6.place(x = 180, y = 445)
    Value7.place(x = 0, y = 360)
    Value8.place(x = 90, y = 360)
    Value9.place(x = 180, y = 360)
    ValuePi.place(x = 300, y = 304)
    ValueAns.place(x = 270, y = 615)
    Valueln.place(x = 375, y = 192)
    Sin.place(x = 225, y = 248)
    Cos.place(x = 300, y = 248)
    Tan.place(x = 375, y = 248)
    Hyp.place(x = 150, y = 248)
    time.place(x = 75, y = 248)
    sto.place(x = 0, y = 304)
    M.place (x = 375, y= 304)
    Brk1.place(x = 150, y = 304)
    Brk2.place(x = 225, y = 304)
    Addition.place(x = 270, y = 530)
    Subtraction.place(x = 360, y = 530)
    Multiplication.place(x = 270, y = 445)
    Division.place(x = 360, y = 445)
    Equal.place(x = 360, y = 615)
    Decimal.place(x = 180, y = 615)
    Negative.place(x = 0, y = 615)
    Inverse.place(x = 75, y= 136)
    Square.place(x = 150, y = 192)
    Power.place(x = 225, y = 192)
    Cube.place(x = 375, y = 136)
    log.place(x = 300, y = 192)
    SqrRoot.place(x = 75, y = 192)
    #Root.place(x = 1, y = 580)
    Left.place(x = 180, y = 150)
    Right.place(x = 244, y = 150)
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
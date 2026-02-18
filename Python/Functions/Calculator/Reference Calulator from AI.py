import tkinter as tk

# --- Functions ---

def click(button_value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(button_value))

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# --- Window Setup ---

root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("320x400")
root.resizable(False, False)

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
display.pack(fill="both", padx=10, pady=10, ipady=10)

# --- Buttons Layout ---

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    
    for button in row:
        if button == "=":
            btn = tk.Button(row_frame, text=button, font=("Arial", 18),
                            command=calculate)
        else:
            btn = tk.Button(row_frame, text=button, font=("Arial", 18),
                            command=lambda b=button: click(b))
        
        btn.pack(side="left", expand=True, fill="both")

# Clear Button
clear_button = tk.Button(root, text="Clear", font=("Arial", 18), command=clear)
clear_button.pack(fill="both", padx=10, pady=5)

root.mainloop()

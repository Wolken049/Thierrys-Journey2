import tkinter as tk
from tkinter import messagebox
def dice():
    import random
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    x = random.randint(1, 6)
    
    if x == 1:
        messagebox.showinfo("Dice Roll", "You rolled a 1!")
    else:
        messagebox.showinfo("Dice Roll", f"You rolled a {x}!")
        
dice()
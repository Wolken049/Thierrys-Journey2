from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title("Simple List App")
root.geometry("300x600")

listbox = tk.Listbox(root, height = 10, width = 30)
listbox.pack(pady = 10)

entry = tk.Entry(root, width = 25)
entry.pack(pady = 5)

def add_item():
    item = entry.get()
    if item:
        listbox
from tkinter import *

def go(event):
    cs = Lb.curselection()

    w.config(text=Lb.get(cs))
    
    for list in cs:
        if list == 0:
            top.configure(background = 'red')
        elif list == 1:
            top.configure(background = 'blue')
        elif list == 2:
            top.configure(background = 'green')
        elif list == 3:
            top.configure(background = 'white')

top = Tk()
top.geometry('250x275')
top.title('Double click')

Lb = Listbox(top, height = 6)

Lb.insert(0, 'Red')
Lb.insert(1, 'Blue')
Lb.insert(2, 'Green')
Lb.insert(3, 'White')

Lb.bind('<Double-1>', go)
Lb.pack()

w = Label(top, text="Default")
w.pack()
top.mainloop()
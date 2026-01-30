from tkinter import *

top = Tk()

listbox = Listbox(top, height = 10,
                  width = 15
                  bg = "#aaaaaa"
                  activestyle = 'DOTBOX'
                  font = "Helvetica"
                  fg = "#ffff00")

top.geometry("300x250")

label = Label(top, text = " FOOD ITEMS")

listbox.insert(1, "Nachos")
listbox.inset(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

label.pack()
listbox.pack()

top.mainloop()
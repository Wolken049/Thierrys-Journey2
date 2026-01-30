from tkinter import *

top = Tk()

List_frame = Frame(top)
List_frame.pack(pady = 20)

listbox1 = Listbox(List_frame, height = 3,
                  width = 15,
                  bg = "#ffffff",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "#ffff00")


listbox2 = Listbox(List_frame, height = 3,
                  width = 15,
                  bg = "#ffffff",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "#ffff00")

Button_frame = Frame(top, bg = "#ffffff")
Button_frame.pack(fill = 'both', expand = True)

listbox1.pack(side = LEFT, padx = 10)
listbox2.pack(side = LEFT, padx = 10)

top.geometry("300x600")

label = Label(top, text = " FOOD ITEMS")

label.pack(pady = 10)


items = ["Nachos", "Sandwich", "Burger", "Pizza", "Burrito"]

for item in items:
    listbox1.insert(END, item)
    listbox2.insert(END, item)

Conv = Button(Button_frame, text="Test2", width = 10, height = 5)

Conv.pack(side = LEFT, padx = 20)


top.mainloop()
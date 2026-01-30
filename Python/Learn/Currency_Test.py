from tkinter import *
import tkinter as tk

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
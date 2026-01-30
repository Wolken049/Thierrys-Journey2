from tkinter import *

application = Tk()
application.geometry("400x700")
application.title("Buttons")
application.config(bg="#000000")

buttom_frame = Frame(application, bg="#ffffff")
buttom_frame.pack(fill = 'both', expand=True)

def myClick1():
    Label1 = Label(application, text="Hii!")
    Label1.pack()
    
def myClick2():
    Label2 = Label(application, text="Hello!")
    Label2.pack()    

Test1 = Button(buttom_frame, text="Test1", command=myClick1 ,padx=60, pady=20, fg = "#333366", bg = "#ccccff")
Test2 = Button(buttom_frame, text="Test2", command=myClick2 ,padx=60, pady=20, fg = "   #333366", bg = "#ccccff")



Test1.place(x = 100, y = 100)
Test2.place(x = 100, y = 200)

application.mainloop()
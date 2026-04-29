from mysql.connector import  connect
from tkinter import *
import tkinter as tk

Defaul_Font = ("Segoe UI", 50)
Button_Font = ("Segoe UI", 20)

application = tk.Tk()
application.geometry("400x700")
application.title("SQL Test")
application.config(bg="#aaaaaa")

Entry_Frame = Frame(application, bg="#ccccdd")
Entry_Frame.pack(fill = 'both', expand = True, padx = 5, pady = 5, ipady = 5)

Button_Frame = Frame(application, bg="#aaaacc")
Button_Frame.pack(fill = 'both', expand = True, padx = 5, pady = 5, ipady = 5)

class Form:
    def __init__(self):
        self.First_Name = Entry(Entry_Frame, font = Defaul_Font, fg="#000000")
        self.Last_Name = Entry(Entry_Frame, font = Defaul_Font, fg="#000000")
        self.Sex = Entry(Entry_Frame, font = Defaul_Font, fg="#000000")
        self.Email = Entry(Entry_Frame, font = Defaul_Font, fg="#000000")
    
    def Get_Base_Info(self):
        return {
            "First_Name": self.First_Name.get(),
            "Last_Name": self.Last_Name.get(),
            "Sex": self.Sex.get(),
            "Email": self.Email.get()
        }
        
class Student(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def Get_Student_Data(self):
        return self.Get_Base_Info()

class Staff(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def Type_Staff(self, Type : str):
        self.Type = Type
    def Get_Staff_Data(self):
        return self.Get_Base_Info()

class Teacher(Staff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Subject = Entry(Entry_Frame)
        self.Classroom = Entry(Entry_Frame)
        
    def Get_Teacher_Data(self):
        Data = super().Get_Staff_Data()
        Data["Subject"] = self.Subject.get()
        Data["Classroom"] = self.Classroom.get()
        
        return Data
    
class Admin(Staff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Department = Entry(Entry_Frame)
    
    def Get_Admin_Data(self):
        Data = super().Get_Staff_Data()
        Data["Department"] = self.Department.get()
        
        return Data

application.mainloop()
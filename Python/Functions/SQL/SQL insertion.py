import os
from dotenv import load_dotenv
from mysql.connector import connect
from tkinter import *
import tkinter as tk

load_dotenv()

#connectin Database

def get_db_connection():
    try:
        return connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_User"),
            password = os.getenv("DB_Pass"),
            database = os.getenv("DB_Name")
        )
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return None

mydb = get_db_connection()

#Retrieves contents within a table. z.B: Students

if mydb and mydb.is_connected():
    mycursor = mydb.cursor()
    mycursor.execute("select * from Students")
    
    for db in mycursor:
        print(db)
    
    mycursor.close()
    mydb.close()
    print("Closed")
    
#Define fonts

Defaul_Font = ("Times New Roman", 15)
Title_Font = ("Times New Roman", 25)

#Creating the GUI

application = tk.Tk()
application.geometry("600x900")
application.title("School Record")
application.config(bg="#aaaaaa")


Form_Frame = Frame(application, bg = "#cccccc")
Form_Frame.pack(fill = "both", expand = True, padx = 5, pady = 5)

Title = Label(Form_Frame, font = Title_Font, text = "Data entry Form",fg = "#000000")
Title.pack(fill = "both", expand = True, padx = 25, pady = 20)
Title.place(x = 180, y = 0)


# Define Form and Entries
class Form:
    def __init__(self):
        self.First_Name = Entry(Form_Frame, font = Defaul_Font,  fg="#000000")
        self.Last_Name = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        self.Sex = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        self.Email = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        self.Age = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        self.Address = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        
        self.First_Name.place(x = 95, y = 120, width = 200, height = 28)
        self.Last_Name.place(x = 390, y = 120, width = 200, height = 28)
        self.Sex.place(x = 50, y = 180, width = 200, height = 28)
        self.Email.place(x = 50, y = 500, width = 500, height = 28)
        self.Age.place(x = 390, y = 180, width = 100, height = 28)
        self.Year.place(x = 95, y = 210, width = 200, height = 28)
        self.Address.place(x = 50, y = 580, width = 500, height = 28)
        
        First_Name_Entry = Label(Form_Frame, font = Defaul_Font, text = "First Name", fg = "#000000")
        Last_Name_Entry = Label(Form_Frame, font = Defaul_Font, text = "Last Name", fg = "#000000")
        Sex_Entry = Label(Form_Frame, font = Defaul_Font, text = "Sex", fg = "#000000")
        Email_Entry = Label(Form_Frame, font = Defaul_Font, text = "Email", fg = "#000000")
        Age_Entry = Label(Form_Frame, font = Defaul_Font, text = "Age", fg = "#000000")
        Year_Entry = Label(Form_Frame, font = Defaul_Font, text = "Year", fg = "#000000")
        Address_Entry = Label(Form_Frame, font = Defaul_Font, text = "Address", fg = "#000000")
        
        First_Name_Entry.place(x = 0, y = 120)
        Last_Name_Entry.place(x = 300, y = 120)
        Sex_Entry.place(x = 0, y = 180)
        Email_Entry.place(relx = 0.5, y = 470)
        Age_Entry.place(x = 0, y = 210)
        Year_Entry.place(x = 300, y = 210)
        Address_Entry.place(x = 275, y = 550)
        

        
    def Get_Base_Info(self):
        return {
            "First_Name": self.First_Name.get(),
            "Last_Name": self.Last_Name.get(),
            "Sex": self.Sex.get(),
            "Email": self.Email.get(),
            "Age": self.Age.get(),
            "Address": self.Address.get()
        }
        
class Student(Form):
    def __init__(self, Grade, **kwargs):
        super().__init__(**kwargs)
        
        
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
        self.Subject = Entry(Form_Frame)
        self.Classroom = Entry(Form_Frame)
        
    def Get_Teacher_Data(self):
        Data = super().Get_Staff_Data()
        Data["Subject"] = self.Subject.get()
        Data["Classroom"] = self.Classroom.get()
        
        return Data
    
class Admin(Staff):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Department = Entry(Form_Frame)
    
    def Get_Admin_Data(self):
        Data = super().Get_Staff_Data()
        Data["Department"] = self.Department.get()
        
        return Data

Form()

application.mainloop()
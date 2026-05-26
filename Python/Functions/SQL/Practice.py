import os
import ctypes
from dotenv import load_dotenv
from mysql.connector import connect
from tkinter import *
import tkinter as tk

load_dotenv()

#connecting Database

def get_db_connection():
    try:
        return connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_User"),
            password = os.getenv("DB_Pass"),
            database = os.getenv("DB_Practice")
        )
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return None

mydb = get_db_connection()

#Retrieves contents within a table. z.B: Students

Defaul_Font = ("Times New Roman", 15)
Title_Font = ("Times New Roman", 25)

#Creating the GUI

application = tk.Tk()
application.geometry("600x900")
application.title("Practice Record")
application.config(bg="#aaaaaa")


Form_Frame = Frame(application, bg = "#cccccc")
Form_Frame.pack(fill = "both", expand = True, padx = 5, pady = 5)

Title = Label(Form_Frame, font = Title_Font, text = "Practice entry Form",fg = "#000000")
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
        self.Year = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        self.Address = Entry(Form_Frame, font = Defaul_Font, fg="#000000")
        
        self.First_Name.place(x = 95, y = 120, width = 200, height = 28)
        self.Last_Name.place(x = 390, y = 120, width = 200, height = 28)
        self.Sex.place(x = 40, y = 180, width = 200, height = 28)
        self.Email.place(x = 50, y = 500, width = 500, height = 28)
        self.Age.place(x = 40, y = 210, width = 100, height = 28)
        self.Year.place(x = 350, y = 210, width = 200, height = 28)
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
        
        #Sex_input = self.Sex.get()
        
        #If statement to confirm if Sex is Male/Female
        
        self.Complete = Button(Form_Frame, font = Defaul_Font, text = "Complete", command=self.Completed)
        self.Complete.place(x = 260, y = 700)
        
    def Get_Base_Info(self):
        return {
            "First_Name": self.First_Name.get(),
            "Last_Name": self.Last_Name.get(),
            "Sex": self.Sex.get(),
            "Email": self.Email.get(),
            "Age": self.Age.get(),
            "Year": self.Year.get(),
            "Address": self.Address.get()
        }
    
    def Completed(self):
        global mydb
        try:
            Data = self.Get_Base_Info()
        
            mycursor = mydb.cursor()

            sql = "INSERT INTO Practice_Table (Fname, Sname, Sex, Email, Age, YEAR, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            val = (
            Data["First_Name"], 
            Data["Last_Name"],
            Data["Sex"],
            Data["Email"],
            Data["Age"],
            Data["Year"],
            Data["Address"]
            )
        
            mycursor.execute(sql, val)
            mydb.commit()
            print("Data successfully committed!")
            
            self.First_Name.delete(0, END)
            self.Last_Name.delete(0, END)
            self.Sex.delete(0, END)
            self.Email.delete(0, END)
            self.Age.delete(0, END)
            self.Year.delete(0, END)
            self.Address.delete(0, END)
        
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"{e}", "Achtung", 0x30)
    
    


Form()

application.mainloop()
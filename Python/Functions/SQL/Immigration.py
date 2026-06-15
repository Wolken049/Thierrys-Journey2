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
            database = os.getenv("DB_Immigration")
        )
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return None

mydb = get_db_connection()

#Global Consonants

DEFAULT_FONT = ("Times New Roman", 20)
DEFAULT_COLOUR = "#000000"
FORM_SIZE = "700x650"

ValidVisa = ["STUDENT", "WORK", "TOURIST"]
ValidReasonOfTravel = ["WORK", "SCHOOL", "TOURING", "CHAPERONE"]

#Creating the GUI



SEX = ["MALE", "FEMALE"]
VISA = ["STUDENT", "WORK", "TOURIST"]

#Define Form and Entries
class Immigrant:
    global DEFAULT_FONT
    def __init__(self):
        self.Immigration = tk.Tk()
        self.Immigration.geometry(FORM_SIZE)
        self.Immigration.title("Immigraion Record")
        self.Immigration.config(bg="#aaaaaa")

        self.Form_Frame = Frame(self.Immigration, bg = "#cccccc")
        self.Form_Frame.pack(fill = "both", expand = True, padx = 25, pady = 20)

        Title = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Immigrant form", fg = DEFAULT_COLOUR)
        Title.pack(fill = "both", expand = True, padx = 25, pady = 20)
        Title.place(x = 238, y = 0)
        
        self.First_Name = Entry(self.Form_Frame, font = DEFAULT_FONT,  fg=DEFAULT_COLOUR)
        self.Last_Name = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR)
        self.Sex = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR, state = "readonly")
        self.Age = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR)
        self.Visa = Entry(self.Form_Frame, font = DEFAULT_FONT, fg = DEFAULT_COLOUR, state = "readonly")
        self.Address = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR)
        self.Reason = Entry(self.Form_Frame, font = DEFAULT_FONT, fg = DEFAULT_COLOUR, state = "readonly")
        
        self.First_Name.place(x = 15, y = 120, width = 300, height = 40)
        self.Last_Name.place(x = 330, y = 120, width = 300, height = 40)
        self.Sex.place(x = 70, y = 180, width = 100, height = 40)
        self.Age.place(x = 280, y = 180, width = 100, height = 40)
        self.Visa.place(x = 530, y = 180, width = 100, heigh = 40)
        self.Reason.place(x = 50, y = 330, width = 550, height = 40)
        self.Address.place(x = 50, y = 450, width = 550, height = 40)

        First_Name_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "First Name", fg = DEFAULT_COLOUR)
        Last_Name_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Last Name", fg = DEFAULT_COLOUR)
        Sex_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Sex", fg = DEFAULT_COLOUR)
        Age_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Age", fg = DEFAULT_COLOUR)
        Visa_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Visa", fg = DEFAULT_COLOUR)
        Reason_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Reason", fg = DEFAULT_COLOUR)
        Address_Label = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Address", fg = DEFAULT_COLOUR)
        
        First_Name_Label.place(x = 80, y = 80)
        Last_Name_Label.place(x =420, y = 80)
        Sex_Label.place(x = 0, y = 180)
        Age_Label.place(x = 225, y = 180)
        Visa_Label.place(x = 450, y = 180)
        Reason_Label.place(x = 280, y = 293)
        Address_Label.place(x = 280, y = 410)
        
        FM_Button = Button(self.Form_Frame, text = "^", command = self.FM_Options)
        FM_Button.pack()
        FM_Button.place(x = 50, y = 180, width = 20, height = 40)
        
        Visa_Button = Button(self.Form_Frame, text = "^", command = self.Visa_Options)
        Visa_Button.pack()
        Visa_Button.place(x = 510, y = 180, width= 20, height = 40)
        
        Reason_Button = Button(self.Form_Frame, text = "^", command = self.Reason_Options)
        Reason_Button.pack()
        Reason_Button.place(x = 30, y = 330, width= 20, height = 40)
        
        self.Complete = Button(self.Form_Frame, font = DEFAULT_FONT, text = "COMPLETE", command = self.Completed)
        self.Complete.place(x = 240, y = 520)
        
        self.Immigration.mainloop()
    
    def FM_Options(self):
        def insert(event):
            chosen = Lb.curselection()
            for list in chosen:
                if list == 0:
                    self.Sex.configure(state = NORMAL)
                    self.Sex.delete(0, END)
                    self.Sex.insert(0, "Male")
                    self.Sex.configure(state = "readonly")
                    Lb.destroy()
                elif list == 1:
                    self.Sex.configure(state = NORMAL)
                    self.Sex.delete(0, END)
                    self.Sex.insert(0, "Female")
                    self.Sex.configure(state = "readonly")
                    Lb.destroy()
        Lb = Listbox(self.Immigration, width = 16, height = 2)
         
        Lb.insert(0, "Male")
        Lb.insert(1, "Female")
        
        Lb.bind('<Double-1>', insert)
        Lb.pack()
        Lb.place(x = 75, y = 240)
        
        
    
    def Visa_Options(self):
        def insert(event):
            chosen = Lb.curselection()
            for list in chosen:
                if list == 0:
                    self.Visa.configure(state = NORMAL)
                    self.Visa.delete(0, END)
                    self.Visa.insert(0, "Student")
                    self.Visa.configure(state = "readonly")
                elif list == 1:
                    self.Visa.configure(state = NORMAL)
                    self.Visa.delete(0, END)
                    self.Visa.insert(0, "Work")
                    self.Visa.configure(state = "readonly")
                elif list == 2:
                    self.Visa.configure(state = NORMAL)
                    self.Visa.delete(0, END)
                    self.Visa.insert(0, "Toursit")
                    self.Visa.configure(state = "readonly")
                    
        Lb = Listbox(self.Immigration, width = 16, height = 2)
         
        Lb.insert(0, "Student")
        Lb.insert(1, "Work")
        Lb.insert(2, "Tourist")
        
        Lb.bind('<Double-1>', insert)
        Lb.pack()
        Lb.place(x = 535, y = 240)
    
    def Reason_Options(self):
        def insert(event):
            chosen = Lb.curselection()
            for list in chosen:
                if list == 0:
                    self.Reason.configure(state = NORMAL)
                    self.Reason.delete(0, END)
                    self.Reason.insert(0, "School")
                    self.Reason.configure(state = "readonly")
                elif list == 1:
                    self.Reason.configure(state = NORMAL)
                    self.Reason.delete(0, END)
                    self.Reason.insert(0, "Work")
                    self.Reason.configure(state = "readonly")
                elif list == 2:
                    self.Reason.configure(state = NORMAL)
                    self.Reason.delete(0, END)
                    self.Reason.insert(0, "Touring")
                    self.Reason.configure(state = "readonly")
                elif list == 3:
                    self.Reason.configure(state = NORMAL)
                    self.Reason.delete(0, END)
                    self.Reason.insert(0, "Chaperone")
                    self.Reason.configure(state = "readonly")
                
        Lb = Listbox(self.Immigration, width = 91, height = 2)
         
        Lb.insert(0, "School")
        Lb.insert(1, "Work")
        Lb.insert(2, "Touring")
        Lb.insert(3, "Chaperone")
        
        Lb.bind('<Double-1>', insert)
        Lb.pack()
        Lb.place(x = 75, y = 385)
        
    def Get_Base_Info(self):
        return {
            "First_Name": self.First_Name.get(),
            "Last_Name": self.Last_Name.get(),
            "Sex": self.Sex.get(),
            "Age": self.Age.get(),
            "Visa": self.Visa.get(),
            "Year": self.Year.get(),
            "Address": self.Address.get(),
            "ReasonOfTravel" : self.Reason.get()
        }
    
    def Completed(self):
        global mydb, SEX, VISA
        try:
            Data = self.Get_Base_Info()
            Age_Verify = self.Age.get()
            Visa_Verify = self.Visa.get()
            Reason_Verify = self.Reason.get()
            
            if self.Age.get() is not int or self.Age.get() < 0:
                ctypes.windll.user32.MessageBoxW(0, "Enter a suitable age", "Achtung", 0x30)
            else:
                if Age_Verify < 18 and Visa_Verify == "Work":
                    ctypes.windll.user32.MessageBoxW(0, 
                                                     "You are too young to apply for a work visa",
                                                     "Achtung",
                                                     0x30)
                elif Age_Verify < 18 and (Reason_Verify == "Work" or Reason_Verify == "Chaperone"):
                    ctypes.windll.user32.MessageBoxW(0,
                                                     f"You are too young to {Reason_Verify}",
                                                     "Achtung",
                                                     0x30)
                
                mycursor = mydb.cursor()

                sql = "INSERT INTO Immigration_Table (Fname, Sname, Sex, Visa, Age, YEAR, Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"

                val = (
                Data["First_Name"], 
                Data["Last_Name"],
                Data["Sex"],
                Data["Visa"],
                Data["Age"],
                Data["Address"],
                Data["ReasonOfTravel"]
                )
            
                mycursor.execute(sql, val)
                mydb.commit()
                print("Data successfully committed!")
                
                
                self.First_Name.delete(0, END)
                self.Last_Name.delete(0, END)
                self.Sex.delete(0, END)
                self.Visa.delete(0, END)
                self.Age.delete(0, END)
                self.Year.delete(0, END)
                self.Address.delete(0, END)
                self.Reason.delete(0, END)
                
                self.Questions = tk.Toplevel()
                self.Questions.geometry("600x300")
                self.Questions.title("Question Record")
                self.Questions.config(bg="#aaaaaa")

                Question_Frame = Frame(self.Questions, bg = "#cccccc")
                Question_Frame.pack(fill = "both", expand = True, padx = 25, pady = 20)

                Question_Title = Label(Question_Frame, font = DEFAULT_FONT, text = "Questions", fg = DEFAULT_COLOUR)
                Question_Title.pack(fill = "both", expand = True, padx = 25, pady = 20)
                Question_Title.place(x = 180, y = 0)
                
                
                self.Guardian_label = Label(Question_Frame, font = DEFAULT_FONT, text = "Are you acommpanying any children?", fg = DEFAULT_COLOUR)
                self.Guardian_label.pack(fill = "both", expand = True, padx = 25, pady = 20)
                self.Guardian_label.place(x = 180, y = 0)
                
                self.Minor_label = Label(Question_Frame, font = DEFAULT_FONT, text = "Are you being acommpanied with any guardian?", fg = DEFAULT_COLOUR)
                self.Minor_label.pack(fill = "both", expand = True, padx = 25, pady = 20)
                self.Minor_label.place(x = 180, y = 0)
                
                self.Guardian_Yes = Button(Question_Frame, font = DEFAULT_FONT, text = "YES", fg = DEFAULT_COLOUR, command = self.parent_yes)
                self.Guardian_No = Button(Question_Frame, font = DEFAULT_FONT, text = "NO", fg = DEFAULT_COLOUR, command = self.Immigration.destroy)
                
                self.Minor_Yes = Button(Question_Frame, font = DEFAULT_FONT, text = "YES", fg = DEFAULT_COLOUR, command = self.parent_yes)
                self.Minor_No = Button(Question_Frame, font = DEFAULT_FONT, text = "NO", fg = DEFAULT_COLOUR, command = self.Immigration.destroy)
                
                
                self.Immigration.destroy()
            
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"{e}", "Achtung", 0x30)

    def parent_yes(self):
        self.Questions.destroy()
        
        Guardian_Form = Guardian(self.Immigration)
    def Type_student(self):
        pass

class Guardian(Immigrant):
    global DEFAULT_FONT, DEFAULT_COLOUR, mydb
    def __init__(self):
        self.Guardian = tk.Tk()
        self.Guardian.geometry(FORM_SIZE)
        self.Guardian.title("Guardian Record")
        self.Guardian.config(bg="#aaaaaa")
        
        self.Form_Frame = Frame(self.Guardian, bg = "#cccccc")
        self.Form_Frame.pack(fill = "both", expand = True, padx = 25, pady = 20)

        Title = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Guardian form", fg = DEFAULT_COLOUR)
        Title.pack(fill = "both", expand = True, padx = 25, pady = 20)
        Title.place(x = 240, y = 0)
        
        self.Email = Entry(self.Form_Frame, font = DEFAULT_FONT,  fg=DEFAULT_COLOUR)
        self.No_Children = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR)
        self.Relationship = Entry(self.Form_Frame, font = DEFAULT_FONT, fg = DEFAULT_COLOUR, state = "readonly")
        self.Email.pack(fill = "both", expand = True, padx = 25, pady = 20)
        self.No_Children.pack(fill = "both", expand = True, padx = 25, pady = 20)
        self.Relationship.pack(fill = "both", expand = True, padx = 25, pady = 20)
        

        Email_Label = Label(self.Form_Frame, text = "Email", font = DEFAULT_FONT)
        No_Children_Label = Label(self.Form_Frame, text = "Number of Children", font = DEFAULT_FONT)
        Relationship_Label = Label(self.Form_Frame, text = "Relationship", font = DEFAULT_FONT)
        Email_Label.pack(fill = "both", expand = True, padx = 25, pady = 20)
        No_Children_Label.pack(fill = "both", expand = True, padx = 25, pady = 20)
        Relationship_Label.pack(fill = "both", expand = True, padx = 25, pady = 20)
        
        Email_Label.place(x = 15, y = 120)
        No_Children_Label.place(x = 15, y = 230)
        Relationship_Label.place(x = 15, y = 340)
        self.Email.place(x = 90, y = 120, width = 300, height = 35)
        self.No_Children.place(x = 250, y = 230, width = 300, height = 35)
        self.Relationship.place(x = 180 , y = 340, width = 300, height = 35)
        
        Relationship_Button = Button(self.Form_Frame, font = DEFAULT_FONT, text = "^", command = self.Relationship_options)
        Relationship_Button.pack()
        Relationship_Button.place(x = 160, y = 340, width = 20, height = 40)
        
        self.Complete = Button(self.Form_Frame, font = DEFAULT_FONT, text = "COMPLETE", command = self.Completed)
        self.Complete.place(x = 240, y = 520)
        
        self.Guardian.mainloop()
    
    def Relationship_options(self):
        def insert(event):
            chosen = Lb.curselection()
            for list in chosen:
                if list == 0:
                    self.Relationship.configure(state = NORMAL)
                    self.Relationship.delete(0, END)
                    self.Relationship.insert(0, "Family")
                    self.Relationship.configure(state = "readonly")
                elif list == 1:
                    self.Relationship.configure(state = NORMAL)
                    self.Relationship.delete(0, END)
                    self.Relationship.insert(0, "Teacher")
                    self.Relationship.configure(state = "readonly")
                elif list == 2:
                    self.Relationship.configure(state = NORMAL)
                    self.Relationship.delete(0, END)
                    self.Relationship.insert(0, "Foster")
                    self.Relationship.configure(state = "readonly")
                elif list == 3:
                    self.Relationship.configure(state = NORMAL)
                    self.Relationship.delete(0, END)
                    self.Relationship.insert(0, "Court Appointment")
                    self.Relationship.configure(state = "readonly")
                elif list == 4:
                    self.Relationship.configure(state = NORMAL)
                    self.Relationship.delete(0, END)
                    self.Relationship.insert(0, "Chaperone")
                    self.Relationship.configure(state = "readonly")
        
        Lb = Listbox(self.Guardian, width = 53, height = 2)
         
        Lb.insert(0, "Family")
        Lb.insert(1, "Teacher")
        Lb.insert(2, "Foster")
        Lb.insert(3, "Court Appointed")
        Lb.insert(4, "Chaperone")
        
        Lb.bind('<Double-1>', insert)
        Lb.pack()
        Lb.place(x = 185, y = 400)
            
    def Child(self):
        for x in range(self.No_Children):
            Immigrant()
            Child_Student(self.Immigration)   
    def Completed(self):
        try:
            Data = self.Get_Base_Info()
            
            if self.No_Children.get() is not int or self.No_Children.get() < 0:
                ctypes.windll.user32.MessageBoxW(0, "Enter the number of children you are with", "Achtung", 0x30)
            else:
                mycursor = mydb.cursor()

                sql = "INSERT INTO Guardian_Table (Email, No_Children, Relationship) VALUES (%s, %s, %s)"

                val = (
                Data["Eamil"], 
                Data["No_Children"],
                Data["Relationship"]
                )
            
                mycursor.execute(sql, val)
                mydb.commit()
                print("Data successfully committed!")
                
                self.Email_Entry.delete(0, END)
                self.No_Children_Entry.delete(0, END)
                
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"{e}", "Achtung", 0x30)
            
        

class Child_Student(Immigrant):
    global DEFAULT_FONT
    def __init__(self):
        self.Immigration = tk.Tk()
        self.Immigration.geometry(FORM_SIZE)
        self.Immigration.title("Guardian Record")
        self.Immigration.config(bg="#aaaaaa")

        Title = Label(self.Form_Frame, font = DEFAULT_FONT, text = "Immigrant form", fg = DEFAULT_COLOUR)
        Title.pack(fill = "both", expand = True, padx = 25, pady = 20)
        Title.place(x = 180, y = 0)
        
        self.Email = Entry(self.Form_Frame, font = DEFAULT_FONT,  fg=DEFAULT_COLOUR)
        self.No_Children = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR)
        self.Email.pack(fill = "both", expand = True, padx = 25, pady = 20)
        self.No_Children.pack(fill = "both", expand = True, padx = 25, pady = 20)

        self.Email_Label = Label(self.Form_Frame, text = "Email", font = DEFAULT_FONT)
        self.No_Children_Label = Label(self.Form_Frame, text = "Number of Children", font = DEFAULT_FONT)
        self.Email_Label.pack(fill = "both", expand = True, padx = 25, pady = 20)
        
        self.Email_Label.place(x = 15, y = 120, width = 300, height = 40)
        self.No_Children_Label.place(x = 15, y = 230, width = 300, height = 40)
        self.Email_Entry.place(x = 15, y = 180, width = 300, height = 40)
        self.No_Children_Entry.place(x = 15, y = 280, width = 100, height = 40)
    
    def Completed(self):
        try:
            Data = self.Get_Base_Info()
            
            if self.No_Children.get() is not int or self.No_Children.get() < 0:
                ctypes.windll.user32.MessageBoxW(0, "Enter the number of children you are with", "Achtung", 0x30)
            else:
                mycursor = mydb.cursor()

                sql = "INSERT INTO Guardian_Table (Email, No_Children, Relationship) VALUES (%s, %s, %s)"

                val = (
                Data["Eamil"], 
                Data["No_Children"],
                Data["Relationship"]
                )
            
                mycursor.execute(sql, val)
                mydb.commit()
                print("Data successfully committed!")
                
                self.Email_Entry.delete(0, END)
                self.No_Children_Entry.delete(0, END)
                
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"{e}", "Achtung", 0x30)
            

Immigrant()
Guardian()

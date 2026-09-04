import os
import ctypes
from dotenv import load_dotenv
from mysql.connector import connect
from tkinter import *
import tkinter as tk
from Config import *


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
        self.Reason.place(x = 50, y = 360, width = 550, height = 40)
        self.Address.place(x = 50, y = 480, width = 550, height = 40)

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
        Reason_Label.place(x = 280, y = 323)
        Address_Label.place(x = 280, y = 440)
        
        self.cities_dict = get_cities()
        
        Keys_var = tk.StringVar(value=list(self.cities_dict))
        
        lb = tk.Listbox(self.Form_Frame, listvariable=Keys_var)
        
        def get_selected_value(event):
            selected_index = lb.curselection()[0]
            display_text = lb.get(selected_index)
            db_code = self.cities_dict.get(display_text)
            
        City_Label = Label(self.Form_Frame, text = "City", font = DEFAULT_FONT, fg = DEFAULT_COLOUR)
        City_Label.place(x = 0, y = 250)
        
        self.City = Entry(self.Form_Frame, font = DEFAULT_FONT, fg=DEFAULT_COLOUR, state = "readonly")
        self.City.place(x = 70, y = 250)
        
        City_Button = Button(self.Form_Frame, text = "^", command = self.City_Options)
        City_Button.pack()
        City_Button.place(x = 50, y = 250, width = 20, height = 40)
        
        FM_Button = Button(self.Form_Frame, text = "^", command = self.FM_Options)
        FM_Button.pack()
        FM_Button.place(x = 50, y = 180, width = 20, height = 40)
        
        Visa_Button = Button(self.Form_Frame, text = "^", command = self.Visa_Options)
        Visa_Button.pack()
        Visa_Button.place(x = 510, y = 180, width= 20, height = 40)
        
        Reason_Button = Button(self.Form_Frame, text = "^", command = self.Reason_Options)
        Reason_Button.pack()
        Reason_Button.place(x = 30, y = 360, width= 20, height = 40)
        
        self.Complete = Button(self.Form_Frame, font = DEFAULT_FONT, text = "COMPLETE", command = self.Completed)
        self.Complete.place(x = 240, y = 550)
        
        self.Immigration.mainloop()
        
    def City_Options(self):
        def insert(event):
            chosen = Lb.curselection()
            if not chosen:
                return
        
            selected_city = Lb.get(chosen[0])
            
            self.City.configure(state = NORMAL)
            self.City.delete(0, END)
            self.City.insert(0, selected_city)
            self.City.configure(state = "readonly")

            Lb.destroy()
            
        Lb = Listbox(self.Immigration, width = 49, height = LIST_HEIGHT)
        
        for city in self.cities_dict.keys():
            Lb.insert(END, city)
        
        Lb.bind("<ButtonRelease-1>", insert)
        Lb.pack()
        Lb.place(x = 85, y = 300)
    
            
    
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
                elif list == 2:
                    self.Sex.configure(state = NORMAL)
                    self.Sex.delete(0, END)
                    self.Sex.insert(0, "Non-Binary")
                    self.Sex.configure(state = "readonly")
                    Lb.destroy()
                elif list == 3:
                    self.Sex.configure(state = NORMAL)
                    self.Sex.delete(0, END)
                    self.Sex.insert(0, "Other")
                    self.Sex.configure(state = "readonly")
                    Lb.destroy()
                elif list == 4:
                    self.Sex.configure(state = NORMAL)
                    self.Sex.delete(0, END)
                    self.Sex.insert(0, "Prefer not to say")
                    self.Sex.configure(state = "readonly")
                    Lb.destroy()
        Lb = Listbox(self.Immigration, width = 16, height = LIST_HEIGHT)
         
        Lb.insert(0, "Male")
        Lb.insert(1, "Female")
        Lb.insert(2, "Non-Binary")
        Lb.insert(3, "Other")
        Lb.insert(4, "Prefer not to say")
        
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
                Lb.destroy()
                    
        Lb = Listbox(self.Immigration, width = 16, height = LIST_HEIGHT)
         
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
                
        Lb = Listbox(self.Immigration, width = 91, height = LIST_HEIGHT)
         
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
        Adult = False
        Student = False
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
            if self.Age.get() >= 18:
                Adult = True
            
            if self.Visa.get() == "Student":
                Student = True
                
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
                
                if Adult is True:
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
                    
                    self.Guardian_Yes = Button(Question_Frame, font = DEFAULT_FONT, text = "YES", fg = DEFAULT_COLOUR, command = self.Guardian_yes)
                    self.Guardian_No = Button(Question_Frame, font = DEFAULT_FONT, text = "NO", fg = DEFAULT_COLOUR, command = self.Immigration.destroy)
                    
                    self.Minor_Yes = Button(Question_Frame, font = DEFAULT_FONT, text = "YES", fg = DEFAULT_COLOUR, command = self.Guardiaan_yes)
                    self.Minor_No = Button(Question_Frame, font = DEFAULT_FONT, text = "NO", fg = DEFAULT_COLOUR, command = self.Immigration.destroy)
                
                if Student is True:
                    if Adult is True:
                        Adult_Student()
                    else:
                        Child_Student()
                
                self.Immigration.destroy()
            
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"{e}", "Achtung", 0x30)

    def Guardian_yes(self):
        self.Questions.destroy()
        Guardian()
        
        
        Guardian_Form = Guardian(self.Immigration)
    def Type_student(self):
        pass      

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

class Adult_Student(Immigrant):
    def __init__(self):
        pass
            

Immigrant()

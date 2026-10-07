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

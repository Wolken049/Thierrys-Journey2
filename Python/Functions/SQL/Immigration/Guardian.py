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

        #Spouse details


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

            if self.No_Children.get() is not int or self.No_Children.get() <= 0:
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

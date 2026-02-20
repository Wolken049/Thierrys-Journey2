import datetime
current_date = datetime.date.today()

class Immigrants:
    def __init__(self, FName: str, SName: str, ID: str, CofO: str, DoArr: datetime.date):
        if not isinstance(DoArr, datetime.date):
            raise TypeError("DoArr must be a datetime.date object")
        if DoArr > datetime.date.today():
            raise ValueError("DoArr cannot be in the future")
        self.FName = FName
        self.SName = SName
        self.ID = ID
        self.CofO = CofO #Country of Origin
        self.DoArr = DoArr #Date of Arrival
    def info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.CofO}), {self.DoArr}"
    
class Legal(Immigrants):
    def __init__(self, Residence: str, Education: str, Work: str, *args, **kwargs):
        self.Residence = Residence
        self.Education = Education
        self.Work = Work
        super().__init__(*args, **kwargs)
    def legal_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.CofO}), {self.DoArr}, {self.Residence}" \
        f"{self.Education}, {self.Work}"
        
class Naturalised(Legal):
    def __init__(self, DoN: datetime.date, isDual: bool, *args, **kwargs): 
        if not isinstance(DoN, datetime.date):
            raise TypeError("DoN must be a datetime.date object")
        if 'DoArr' in kwargs and DoN < kwargs['DoArr']:
            raise ValueError("DoN cannot be earlier than DoArr")
        self.DoN = DoN #Date of Naturalisation
        self.isDual = isDual #Dual citizen
        super().__init__(*args, **kwargs)
    def naturalised_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.CofO}), {self.DoArr}, {self.Residence}" \
        f"{self.Education}, {self.Work}, {self.DoN}, {self.isDual}"
    
class Illegal(Immigrants):
    def __init__(self, DoR: datetime.date, Group: str, Discover_Location: str, *args, **kwargs):
    #DoR = Date of Return
        self.DoR = DoR
        self.Group = Group
        self.Discover_Location = Discover_Location
        if 'DoArr' in kwargs == "N/A":
            pass
        if not str(DoR) >= str(datetime.date.today()):
            raise ValueError(f"Invalid return date: The return date must be today or later")
        super().__init__(*args, **kwargs)
    def illegal_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.CofO}), {self.DoArr}, {self.DoR}, {self.Group}, " \
            f"{self.Discover_Location}"
class Refugee(Immigrants):
    def __init__(self, RoR: str, DoAp: datetime.date, *args, **kwargs):
    #RoR = Reason of Refuge
    #DoAp = Date of Approval
        self.RoR = RoR
        self.DoAp = DoAp
        super().__init__(*args, **kwargs)
    def refugee_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.CofO}), {self.DoArr}, {self.RoR}, {self.DoAp}"
    
Jack = Immigrants("Jack", "Spelamann", "US04765", "United States of America", datetime.date(2025, 12, 1))
Jamal = Illegal("Jamal", "Owoko", "NG0034", "Nigeria", "N/A", datetime.date(2026, 3, 5), "N/A", "Dresden")

print(Jack.CofO)
print(Jamal.DoArr)



import datetime
current_date = datetime.date.today()

class Immigrants:
    def __init__(self, FName: str, SName: str, ID: str, Country_Origin: str, DateofArrival: datetime.date):
        if not isinstance(DateofArrival, datetime.date):
            raise TypeError("DateofArrival must be a datetime.date object")
        if DateofArrival > datetime.date.today():
            raise ValueError("DateofArrival cannot be in the future")
        self.FName = FName
        self.SName = SName
        self.ID = ID
        self.Country_Origin = Country_Origin
        self.DateofArrival = DateofArrival
    def info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.Country_Origin}), {self.DateofArrival}"
    
class Legal(Immigrants):
    def __init__(self, Residence: str, Education: str, Work: str, *args, **kwargs):
        self.Residence = Residence
        self.Education = Education
        self.Work = Work
        super().__init__(*args, **kwargs)
    def legal_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.Country_Origin}), {self.DateofArrival}, {self.Residence}" \
        f"{self.Education}, {self.Work}"
        
class Naturalised(Legal):
    def __init__(self, DoN: datetime.date, isDual: bool, *args, **kwargs): 
        if not isinstance(DoN, datetime.date):
            raise TypeError("DoN must be a datetime.date object")
        if 'DateofArrival' in kwargs and DoN < kwargs['DateofArrival']:
            raise ValueError("DoN cannot be earlier than DateofArrival")
        self.DoN = DoN
        self.isDual = isDual
        super().__init__(*args, **kwargs)
    def naturalised_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.Country_Origin}), {self.DateofArrival}, {self.Residence}" \
        f"{self.Education}, {self.Work}, {self.DoN}, {self.isDual}"
    
class Illegal(Immigrants):
    def __init__(self, DoR: datetime.date, Group: str, Discover_Location: str, *args, **kwargs):
    #DoR = Date of Return
        self.DoR = DoR
        self.Group = Group
        self.Discover_Location = Discover_Location
        if not DoR >= current_date:
            raise ValueError(f"Invalid return date: The return date must be today or later")
        super().__init__(*args, **kwargs)
    def illegal_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.Country_Origin}), {self.DateofArrival}, {self.DoR}, {self.Group}, " \
            f"{self.Discover_Location}"
class Refugee(Immigrants):
    def __init__(self, RoR: str, DoAp: datetime.date, *args, **kwargs):
    #RoR = Reason of Refuge
    #DoAp = Date of Approval
        self.RoR = RoR
        self.DoAp = DoAp
        super().__init__(*args, **kwargs)
    def refugee_info(self):
        return f"{self.FName}, {self.SName}, {self.ID}, ({self.Country_Origin}), {self.DateofArrival}, {self.RoR}, {self.DoAp}"



import datetime
current_year = datetime.datetime.now().year

MClass = ["A-Class", "B-Class", "C-Class", "E-Class", "S-Class", "G-Class", "GLA", "GLC", "GLE", "GLS", "CLA", "CLS", "SL", "SLC", "SLS"]
MTrim = ["180", "200", "220", "250", "280", "300", "320", "350", "400", "450", "500", "550", "580", "600", "53", "54", "63", "65"]
MSub = ["AMG", "Maybach", "EQ"]
Eq = ["EQC", "EQA", "EQB", "EQS", "EQE"]

class Mercedes:
    def __init__(self, Class, Trim, Year):
        if Class not in MClass:
            if Class in Eq:
                raise ValueError(f"{Class} is an EQ model. Please use the SubBrand class to create EQ models. For example write in Class 'A' then in SubBrandName 'EQ'.")
            else:
                raise ValueError(f"Invalid Class: {Class}. Must be one of {MClass}.")
        if Trim not in MTrim:
            raise ValueError(f"Invalid Trim: {Trim}. Must be one of {MTrim}.")
        if not (1900 <= Year <= current_year):
            raise ValueError(f"Year must be between 1900 and {current_year}.")
        self.Class = Class
        self.Trim = Trim
        self.Year = Year
    
    def CarInfo(self):
        return f"{self.Class} {self.Trim} ({self.Year})"
    
class SubBrand(Mercedes):
    def __init__(self, Class, Trim, Year, SubBrandName):
        self.SubBrandName = SubBrandName
        
        if not SubBrandName in MSub:
            raise ValueError(f"Invalid SubBrand: {SubBrandName}. Must be one of {MSub}.")
        super().__init__(Class, Trim, Year)
        
    def SubInfo(self):
        return f"{self.SubBrandName}, {self.Class}, {self.Trim}, ({self.Year})"

try:
    MyCarInput = input("Enter your car details (Class, Trim, Year) separated by commas: ")
    Class, Trim, Year = [item.strip() for item in MyCarInput.split(",")]
    Year = int(Year)
    MyCar = Mercedes(Class, Trim, Year)
    DreamCar = SubBrand("S-Class", "350", 2021, "AMG")

    print(DreamCar.SubInfo())
    print(MyCar.CarInfo())
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
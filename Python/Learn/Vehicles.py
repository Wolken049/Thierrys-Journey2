class Car:
    def __init__(self, Brand, Model, Year, Color):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Color = Color
    def move(self):
        print("Driving...")
    def stop(self):
        print("Stopping...")

class Boat:
    def __init__(self, Brand, Model, Year, Color):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Color = Color
    def move(self):
        print("Sailing...")
    def stop(self):
        print("Anchoring...")

class Plane:
    def __init__(self, Brand, Model, Year, Color):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Color = Color
    def move(self):
        print("Flying...")
    def stop(self):
        print("Landing...")
    
car1 = Car("Toyota", "Corolla", 2020, "Blue")
boat1 = Boat("Yamaha", "212X", 2019, "White")
plane1 = Plane("Boeing", "747", 2018, "Silver")

for vehicle in (car1, boat1, plane1):
    print(f"{vehicle.Brand} {vehicle.Model} ({vehicle.Year}) - {vehicle.Color}")
    vehicle.move()
    vehicle.stop()
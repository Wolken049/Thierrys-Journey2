class Flight:
    def __init__(self, flightID, NoC, flightCrew, NoP, flightPassangers):
        self.self = self
        self.flightID = flightID
        self.NoC = NoC #Number of Crew
        self.flightCrew = flightCrew
        self.NoP = NoP #Number of Passanger
        self.flightPassangers = flightPassangers
    
    def FlightInfo(self):
        return f"{self.flightID}, {self.NoC}, {self.flightCrew}, {self.NoP}, {self.flightPassangers}"

Boeing = Flight("BW214", "10", "N/A", "350", "N/A")
print(Boeing)
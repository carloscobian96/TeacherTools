import math 

class ExperimentData:
    def __init__(self, Gunname:str, Guncartridge:str, Round:str, RoundVelocity_ms:int, Building:str, BuildingHeight_m:int, planet:str):
      self.Gunname = Gunname
      self.Guncartridge = Guncartridge
      self.Round = Round
      self.RoundVelocity_ms = RoundVelocity_ms
      self.Building = Building
      self.BuildingHeight_m = BuildingHeight_m
      self.planet = planet


    def getTime(self):
        return (math.sqrt(2 * self.BuildingHeight_m / self.getGravity))

    def getDistance(self):
        return(self.RoundVelocity_ms * self.getTime())

    def getGravity(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return g_ms2[planets.index(self.planet)]

    def run(self):
        print(f"""Chris is planning on hitting a bottle used as a target for practicing whic is located on Central park.
    He will use an {self.Gunname} which uses a cartridge of {self.Guncartridge}. 
    The round of this weapon is {self.Round}and the velocity of the round is {self.RoundVelocity_ms}m/s.
    He will shoot the gun from {self.Building}, this building has a height of {self.BuildingHeight_m}m.
    The planet in which he is going to shoot is {self.planet}, the gravity is {self.getGravity}.
    The time it will take the gun to hit the bottle is {self.getTime}
    and the distance it will run is {self.getDistance}. Chris just hit the bottle.
    """)



      


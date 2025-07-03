import math
class ExperimentData:
        def __init__(self, Gunname:str, Guncartridge:str, Round:str, ammo_speed:float, building:str, bulding_height_M:float, planet:str):
            self.Gunname = Gunname
            self.Guncartridge = Guncartridge
            self.Round = Round
            self.ammo_speed = ammo_speed
            self.building = building
            self.bulding_height_M = bulding_height_M
            self.planet = planet

        def getTime(self):
            return math.sqrt(2*self.bulding_height_M/self.getGravity())
        
        def getDistance(self):
            return (self.ammo_speed * self.getTime())
        
        def getGravity(self):
            planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
            g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

            return g_ms2[planets.index(self.planet)]

        def run(self):
            print(f""" I shot a projectile from {self.building}, its {self.bulding_height_M} meters tall. 
            Said projectile was a {self.Guncartridge} fired from a {self.Gunname}. It travelled {self.getDistance()} 
            at {self.ammo_speed} m/s^2 for {self.getTime():.2}. It was fired at {self.planet} where the gravity is {self.getGravity()}""" )
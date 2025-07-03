import math
class ExperimentData: 
    def __init__(self, Gunname:str, Cartridgecalibre:str, Round:str, Projectilespeed:float, Building:str, Buildingheight:float, planet:str):
        self.Gunname = Gunname
        self.Cartridgecalibre = Cartridgecalibre
        self.Round = Round
        self.Projectilespeed = Projectilespeed
        self.Building = Building
        self.Buildingheight = Buildingheight
        self.planet = planet
    
    #define time
    def getTime(self):
        return math.sqrt(2 * self.Buildingheight / self.getGravity())
    
    #define distance
    def getDistance(self):
        return(self.Projectilespeed *self.getTime())
    
    #define gravity
    def getGravity(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return g_ms2[planets.index(self.planet)]

    #define the paragraph
    def run(self):
          print(f"""I shot a bullet from {self.Building}, the height is {self.Buildingheight}. It takes {self.getTime()} to reach the ground if you are shooting from the top of the {self.Building} because it's {self.Projectilespeed} fast and it have a distance of {self.getDistance}. The projectile was fired from {self.planet} with a gravity of {self.getGravity()}""")
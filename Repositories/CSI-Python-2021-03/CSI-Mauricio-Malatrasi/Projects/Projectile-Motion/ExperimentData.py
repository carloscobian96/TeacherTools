import math
class ExperimentData:
    def __init__(self, Gunname:str, Guncartridge:str, Round:str, Roundvelocity:float, Building:str, Buildingheight:float, planet:str):
        self.Gunname = Gunname
        self.Guncartridge = Guncartridge
        self.Round = Round
        self.Roundvelocity = Roundvelocity
        self.Building = Building
        self.Buildingheight = Buildingheight
        self.planet = planet
    
    #Define Time
    def getTime(self):
        return (math.sqrt(2 * self.Buildingheight / self.getGravity()))
    
    #Define Distance
    def getDistance(self):
        return(self.Roundvelocity * self.getTime())
    
    #Define Planets with their gravity
    def getGravity(self):
        planets = ["Venus", "Earth", "Saturn", "Neptune", "Jupiter", "Uranus", "Mars", "Pluto"]
        g_ms2 = [8.87, 9.81, 10.44, 11.15, 24.79, 8.69, 3.711, 0.62]
        return g_ms2[planets.index(self.planet)]

    #Paragraph
    def run(self):
        print(f"""I shot a projectile from {self.Building}, it's {self.Buildingheight} meters high. It goes at {self.Roundvelocity} and it takes about {self.getTime():.2} seconds to reach the ground. The distance covered is {self.getDistance()}. It was fired from {self.planet} with a gravity of {self.getGravity()}.""") 
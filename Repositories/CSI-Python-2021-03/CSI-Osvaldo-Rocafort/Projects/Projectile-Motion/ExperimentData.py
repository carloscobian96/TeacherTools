import math 
class ExperimentData: 
    def __init_(self, Gunname:str, Cartrigecalibre:str, Round:str, Roundvelocity:int, Building:str, Buildingheight:int, gravity:int ):
        self.Gunname = Gunname
        self.Cartridgecalibre = Cartrigecalibre
        self.Round = Round 
        self.Roundvelocity = Roundvelocity
        self.Building = Building
        self.Buildingheight = Buildingheight
        self.gravity = gravity

    def getTime(self):
        return (math.sqrt(2 * self.Buildingheight / self.getGravity()))

    def getDistance(self):
        return (self.Roundvelocity * self.getTime)
        
    def getGravity(self):
        planets = ["Earth", "Mercury", "Venus", "Jupiter", "Mars", "Uranus", "Saturn"]
        g_ms2 = [9.81, 3.7, 8.87, 24.79, 10.44, 11.15, 8.69]
        return g_ms2[planets.index(self.planet)]

def run(self):
        print (f"I shot a {self.Gunname} from {self.Building} and the {self.Buildingheight} meters high. It goes at {self.Roundvelocity} and it takes about{self.getTime()} seconds to reach {self.getDistance()}.")



        
 






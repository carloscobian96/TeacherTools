import math 

class ExperimentalData:
    def __init__(self, gun: str, cartridge: str, ammunitionType: str, velocity: float, buildingName: str, buildingHeight: float, planet: float):
        self.gun = gun
        self.cartridge = cartridge
        self.ammunitionType = ammunitionType 
        self.velocity = velocity
        self.buildingName = buildingName
        self.buildingHeight = buildingHeight
        self.planet = planet

#change time into getter
    def getTime(self):
        return (math.sqrt(2 * self.buildingHeight / self.getGravity()))
#set distance into a getter
    def getDistance(self):
        return(self.velocity * self.getTime())
  #set gravity into a getter  
    def getGravity(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return g_ms2[planets.index(self.planet)]
        #Set each plannet's force of gravity
    
    def run(self):
        print(f"The gun is the {self.gun}. The cartridge is the {self.cartridge} and its ammunition type is {self.ammunitionType}. The velocity of the the bullet is {self.velocity}m/s. If I shoot from the top of {self.buildingName} and its height is {self.buildingHeight}m, and it is being shot from {self.planet}. Taking in to consideration that there isnt any air resistance and the height of the building, the time traveled is {self.getTime()}s and the distance traveled would be {self.getDistance()}m")
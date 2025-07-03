import math


import math
class ExperimentData:
    def __init__(self, gun: str, cartridge: str, ammunition: str, velocity: float, buildingName: str, buildingHeight: float, planet: float):
        self.gun=gun
        self.cartridge=cartridge
        self.ammunition=ammunition
        self.velocity=velocity
        self.buildingName=buildingName
        self.buildingHeight=buildingHeight
        self.planet= planet

    def getTime(self):
        return (math.sqrt(2 * self.buildingHeight)/ self.getGravity())

    def getDistance(self):
        return(self.velocity * self.getTime())

    def getGravity(self):
        planets = ("Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune")
        g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return g_ms2[planets.index(self.planet)]

    def run(self):
        print(f"The weapon i choose was {self.gun} and the cartridge of the gun is {self.cartridge}. This cartridge has this type of ammunition {self.ammunition}, the velocity of this ammunition is {self.velocity}m/s. The building I choose was {self.buildingName} and it has a height of {self.buildingHeight}m. The bullet will travel for this much time {self.getTime()} and for this distance {self.getDistance()}. There is no air resistance therefore it wont affect the time and distance it will travel. It is being shot from {self.planet}")









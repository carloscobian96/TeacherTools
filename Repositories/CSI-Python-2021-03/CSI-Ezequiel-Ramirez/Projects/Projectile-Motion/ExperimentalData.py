import json
import math
#Module 6
class ExperimentalData:
    def __init__(self, WeaponName:str, CartridgeCaliber:str, AmmunitionType:str, Velocity:int, BuildingName:str, BuildingHeight:int, Planet:int): 

        self.WeaponName = WeaponName
        self.CartridgeCaliber = CartridgeCaliber
        self.AmmunitionType = AmmunitionType
        self.Velocity = Velocity
        self.BuildingName = BuildingName
        self.BuildingHeight = BuildingHeight
        self.Planet = Planet

    def GetTime(self):
        return(round(math.sqrt(2 * self.BuildingHeight/self.GetGravity()), 2))

    def GetDistance(self):
        return(round(self.Velocity * self.GetTime(), 2))

    def GetGravity(self):
        Planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
        g_ms2 = (3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15)
        return g_ms2[Planets.index(self.Planet)]
    
    def Run(self):
        print(f"For this project, the projectile weapon being utilized is an {self.WeaponName} assault rifle. The cartridge caliber for this gun is {self.CartridgeCaliber}. The only type of round this gun is compatible with is {self.AmmunitionType}. This type of bullets projectile velocity is {self.Velocity} miles per second. The gun is going to be fired off of the {self.BuildingName}, which is {self.BuildingHeight} meters high. After testing, the bullets flied for {self.GetTime()} seconds and travelled {self.GetDistance()} meters under the standard fall of gravity of {self.GetGravity()} meters per second.")
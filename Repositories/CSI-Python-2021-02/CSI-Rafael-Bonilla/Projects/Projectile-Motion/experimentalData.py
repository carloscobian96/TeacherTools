import math

class ExperimentalData:
    def __init__(self, Gun:str, Calliber:str, Bullet:str, BulletVelocityms:str, Building:int, Buildingheight_m:int, planet:int):
            self.Gun = Gun
            self.Calliber = Calliber
            self.Bullet = Bullet
            self.BulletVelocityms = BulletVelocityms
            self.Building = Building
            self.Buildingheight_m = Buildingheight_m
            self.planet = planet
        


#To calculate time we will define "getTime" so we can get it

    def getTime(self):
        return (math.sqrt(2 * self.Buildingheight_m / self.getGravity()))


#To calculate distance we will define "getDistance" so we can get it

    def getDistance(self):
        return (self.BulletVelocityms * self.getTime())


#To calculate gravity we will define "getGraviry" so we can get it

    def getGravity(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return g_ms2[planets.index(self.planet)]
    

#In the "toString" function we will describe the outcome of the experiment

    def toString(self):
        print(f"""I shot a {self.Gun} with a calliber of {self.Calliber} from {self.Building}, it's height was {self.Buildingheight_m}. What we 
    needed to do is measure the time and distance that the bullet traveled, and to how it would be in other planets like {self.planet}. 
    The Bullet that we will be using will be {self.Bullet} which will be going at a velocity of {self.BulletVelocityms}. """)


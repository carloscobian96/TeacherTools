:import math

# This is the external code needed to make the .json class in the projectile function.
# It reuses the previously established parameters to classify them together in a list.

class ExperimentData:
    def __init__(self,ProjectileGun:str, ProjectileCartridge:str, Velocity: int, BuildingLocation:str, BuildingHeight:int, planet:str):
        self.ProjectileGun = ProjectileGun
        self.ProjectileCartridge = ProjectileCartridge
        self.Velocity = Velocity
        self.BuildingLocation = BuildingLocation
        self.BuildingHeight = BuildingHeight
        self.planet = planet
        
        

    def getTime(self):
        return (math.sqrt(2*self.BuildingHeight / self.getGravity()))

    def getDistance(self):
        return (self.Velocity * self.getTime())

    def getGravity(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return g_ms2[planets.index(self.planet)]
    
    

    def run(self):
        print(f"For the purpose of this experiment, I shot a {self.ProjectileCartridge} bullet from a {self.ProjectileGun} from the roof of {self.BuildingLocation} to determine the final velocity of a projectile.")
        print(f"It was under the gravitational acceleration of {self.getGravity()} m/s^2.")
        print(f"It also held a velocity of {self.Velocity} meters per second and was shot from a height of {self.BuildingHeight} meters.")
        print(f"Using these variables, I calculated the distance of the bullet by first finding the time it took to land, which was {self.getTime()} seconds.")
        print(f"After this, I gathered the time and multiplied it with the initial velocity, to find that the projectile had a distance of {self.getDistance()} m.")
        print(f"In conclusion, I was able to determine the distance of my {self.ProjectileGun}'s projectile by gathering its given values to first find the estimated time it would take to land, and then apply it to its initial velocity.\n")







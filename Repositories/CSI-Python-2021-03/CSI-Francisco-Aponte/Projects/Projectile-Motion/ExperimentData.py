import math

# Defining each parameter
class ExperimentData:
    def __init__(self,gun: str, cartridge: str, bullet: str, velocity: float, buildingName: str, buildingHeight: float, planet: str):
        self.gun = gun
        self.cartridge = cartridge
        self.bullet = bullet
        self.velocity = velocity
        self.buildingName = buildingName
        self.buildingHeight = buildingHeight
        self.planet = planet
        # self.gravity = gravity

    # Here im telling the program to solve for time depending on the gravity
    def solveForTime(self):
        return (math.sqrt(2 * self.buildingHeight / self.solveForGravity()))

    #Here im telling the program to solve for the distance on a panet
    def solveForDistance(self):
        return(self.velocity * self.solveForTime())

    #Here im telling the program to solve for the distance of the bullet on earth
    def solveForEarthDistance(self):
        return(self.velocity * (math.sqrt(2 * self.buildingHeight / 9.81)))
    
    #Here im telling the program to solve for the gravity depending on the planet
    def solveForGravity(self):
        planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        gravity_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
        return gravity_ms2[planets.index(self.planet)]

    # Here im telling the program to write the paragraph and use the outputs it just got to implement them into the paragraph
    def run(self):
        print(f"In this experiment, we are climbing {self.buildingHeight} meters to the top of {self.buildingName} and shooting a {self.gun} with a cartidge of {self.cartridge} using a {self.bullet}. Considering there is no air resistance, the bullet will travel with a velocity of {self.velocity} m/s and a distance of {round(self.solveForEarthDistance(), 2)} meters. If we shoot the same gun from {self.planet} that has a gravity of {self.solveForGravity()}, It will travel for a distance of {round(self.solveForDistance(), 2)}meters. ")



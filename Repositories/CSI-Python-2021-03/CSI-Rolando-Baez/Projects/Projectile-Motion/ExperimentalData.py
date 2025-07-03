import math
class ExperimentalData:
    def __init__(self, Gun:str, GunCartrige:str, Round:str, Projectilespeed:float, Building:str, Height:float, Planet:str):
        self.Gun = Gun
        self.GunCartrige = GunCartrige
        self.Round = Round
        self.Projectilespeed = Projectilespeed
        self.Building = Building
        self.Height = Height
        self.Planet = Planet

    def getTime(self):
        return math.sqrt(2 * self.Height / self.getGravity())

    def getDistance(self):
        return(self.Projectilespeed * self.getTime())

    def getGravity(self):
        planets = ['Earth', 'Mars', 'Mercury', 'Saturn', 'Uranus', 'Venus', 'Jupiter', 'Neptune']
        g_ms2 = [9.8, 3.7, 3.7, 10.4, 8.9, 8.9, 24.8, 11.2]
        return g_ms2[planets.index(self.planet)]

        def run(self):
            print(f"""I shot a projectile from {self.Building}, it's {self.Height} meters high.
            It goes at {self.Projectilespeed} and it takes about {self.getTime():.2} for it to travel it's distance
            The distance covered is {self.getDistance()}.
            It was fired from {self.Planet} with a gravity of {self.getGravity()}.""")


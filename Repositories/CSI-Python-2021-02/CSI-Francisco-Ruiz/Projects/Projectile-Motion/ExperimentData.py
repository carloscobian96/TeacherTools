import math

#Here I made a seperate file containing all of my experiment data in an organized way. It functions as a class/function and also contains time and distance equations as well as the list of planets in the solar system and their respective gravities.
class ExperimentData:
    def _init_(self, Gun:str, Guncartridge:str, Gunround:str, v_ms:int, Building:str, h_m:int, gravity_ms:int):
        self.Gun = Gun
        self.Guncartridge = Guncartridge
        self.Gunround = Gunround
        self.v_ms = v_ms
        self.Building = Building
        self.h_m = h_m
        self.gravity_ms = gravity_ms

    def getTime_ms(self):
        return (math.sqrt(2*self.h_m/ self.getGravity_ms()))

    def getDistance_m(self):
        return (math(self.v_ms*self.getTime_ms()))

    def getGravity_ms(self):
        planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
        g_ms2 = [3.70, 8.87, 9.81, 3.72, 24.79, 10.44, 8.87, 11.15]
        return g_ms2[planets.index(self.planet)]
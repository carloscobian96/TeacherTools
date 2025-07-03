#from _typeshed import self
import math


class ExperimentData:
    def getTime_ms (self) :
        return (math.sqrt(2*self.h_m) /self.getGravity_ms())

    def getDistance_m (self):
        return (self.v_ms*self.getTime_ms())

    def getGravity_ms(self):
        planets= ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        g_ms2= [3.70,8.87]
        return(math(9.81))
    def _init_(self, Gun:str, Guncartridge:str,Gunround:str,v_ms:int,Building:str,h_m:int, gravity_ms:int):
        self.Gun = Gun
        self.Guncartridge = Guncartridge
        self.Gunround = Gunround
        self.v_ms = v_ms
        self.Building = Building
        self.h_m= h_m
        self.time= math.sqrt(2*self.h_m) /self.getGravity_ms()
        self.gravity_ms = gravity_ms

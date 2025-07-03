import math
class ExperimentalData:
    def __init__(self, gun:str, CartridgeCalibre:str, ammunition:str, ProjectileVelocity_mps:float, building:str, buildingHeight_m:float, planet:str):
        self.gun = gun
        self.CartridgeCalibre = CartridgeCalibre
        self.ammunition = ammunition
        self.ProjectileVelocity_mps = ProjectileVelocity_mps
        self.building = building
        self.buildingHeight_m = buildingHeight_m
        self.planet = planet
        
    
#función para calcular tiempo
    def calculateTime(self):
        return (math.sqrt((2*self.buildingHeight_m)/self.calculateGravity()))
#función para calcular distancia
    def calculateDistance(self):
        return(self.ProjectileVelocity_mps * self.calculateTime())
#funcion para nombrar cada planeta con una gravedad
    def calculateGravity(self):
        planets =["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urnaus","Neptune"]
        gravity_ms2 =[3.7,8.87,9.81,3.711,24.79,10.44,8.69,11.15]
        return gravity_ms2[planets.index(self.planet)]
#función para imprimir el parrafo descriprivo
    def run(self):
        print(f"We will shoot the {self.gun} from {self.building}, which is {self.buildingHeight_m}m high. The {self.gun}'s catridge calibre is {self.CartridgeCalibre} and it is using the {self.ammunition} bullets. The {self.gun} shoots at {self.ProjectileVelocity_mps} m/s, it took { round(self.calculateTime(), 2) } seconds to hit the ground and it traveled {round(self.calculateDistance(), 2) } meters. It was shot from {self.planet}, which has a gravity of {self.calculateGravity()} meters per square second.\n")


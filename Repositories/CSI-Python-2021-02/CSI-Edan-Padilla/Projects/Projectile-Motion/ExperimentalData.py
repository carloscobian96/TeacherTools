import math 
class ExperimentData: 
    def __init__(self,Gunname:str,Guncaliber:str, Round:str, Roundvelocity:str, Building:int, Buildingheight_m:int, Planet:int):
        self.Gunname = Gunname 
        self.Guncaliber = Guncaliber
        self.Round = Round
        self.Roundvelocity = Roundvelocity
        self.Building = Building
        self.Buildingheight_m = Buildingheight_m
        self.Planet = Planet 
    
    #To calculate time we will define "GetTimme" so we can get it

    def GetTime(self): 
        return (math.sqrt(2*self.Buildingheight_m/self.GetGravity()))

    #To calculate distance we will difine "GetDistance" so we can get

    def GetDistance(self):
        return (self.Roundvelocity*self.GetTime)

    #To calculate gravivity we will define "GetGravity" so we can get it

    def GetGravity(self):
        Planets = ["Mercury","Vinus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
        G_ms2 = [3.7,8.87,9.81,3.711,24.79,10.44,8.69,11.15]
        return G_ms2[Planets.index(self.Planet)]
    
    #In the "ToString" fiunction we will describe the outcome of the experiment

    def ToString(self):
        print(f" In this experimetn i will be shooting a un from a building. The gun that I used was {self.Gunname}. TZhe bullet that I used was {self.Round} and the calliber of the gun is {self.Guncaliber}. The building is {self.Building} and the height of the building is {self.Buildingheight_m}. The bullet has a speed of {self.Roundvelocity}. The world was a gravity of {self.Planet}.")

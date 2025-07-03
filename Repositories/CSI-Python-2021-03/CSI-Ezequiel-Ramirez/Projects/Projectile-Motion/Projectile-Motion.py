import math
import fractions
import json
from pathlib import Path
import os

WeaponName = "ASh-12"
CartridgeCaliber = "12.7x55mm"
AmmunitionType = "12.7x55mm STs-130"
Velocity = 285 #m/s
BuildingName = "Lotte World Tower"
BuildingHeight = 555 #m
Gravity = 9.8 #m/s

Time = round((math.sqrt((2 * -555) / -9.8)), 2) #Formula to determine amount of time
print(f"The time is {Time} seconds.")

Distance = round((Velocity) * (Time), 2) #Formula to determine the distance
print(f"The projectile will travel {Distance} meters.")

print(f"For this project, the projectile weapon being utilized is an {WeaponName} assault rifle. The cartridge caliber for this gun is {CartridgeCaliber}. The only type of round this gun is compatible with is {AmmunitionType}. This type of bullets projectile velocity is {Velocity} miles per second. The gun is going to be fired off of the {BuildingName}, which is {BuildingHeight} meters high. After testing, the bullets flied for {Time} seconds and travelled {Distance} meters under the standard fall of gravity of {Gravity} meters per second.")

def Weapon(WeaponName:str, CartridgeCaliber:str, AmmunitionType:str, Velocity:int, BuildingName:str, BuildingHeight:int, Time:int, Distance:int, Gravity:int):
    print(f"The time is {Time} seconds.")
    print(f"The projectile will travel {Distance} meters.")
    print(f"For this project, the projectile weapon being utilized is an {WeaponName} assault rifle. The cartridge caliber for this gun is {CartridgeCaliber}. The only type of round this gun is compatible with is {AmmunitionType}. This type of bullets projectile velocity is {Velocity} miles per second. The gun is going to be fired off of the {BuildingName}, which is {BuildingHeight} meters high. After testing, the bullets flied for {Time} seconds and travelled {Distance} meters under the standard fall of gravity of {Gravity} meters per second.")

ExperimentData = {
    "WeaponName" : "ASh-12",
    "CartridgeCaliber" : "12.7x55mm",
    "AmmunitionType" : "12.7x55mm STs-130",
    "Velocity" : 285, #m/s
    "BuildingName" : "Lotte World Tower",
    "BuildingHeight" : 555, #m
    "Time" : (round(math.sqrt((2 * -555) / -9.8)), 2), #s
    "Distance" : (round(Velocity) * (Time), 2), #m
    "Gravity" : 9.8 #m/s
}

import ExperimentalData
from ExperimentalData import ExperimentalData

##def Experiment(experimentalData:ExperimentalData):
   ## time = round(math.sqrt(2 * experimentalData.BuildingHeight/experimentalData.Gravity), 2)
    ##DeltaX = round(experimentalData.Velocity * time, 2)
   ## print(f"For this experiment I shot an {experimentalData.WeaponName} from the {experimentalData.BuildingName}, which is located {experimentalData.BuildingHeight} meters high, which after being shot with the standard gravity of {experimentalData.Gravity} meters per second, flies for {time} seconds at {DeltaX} meters per second.")

myData = ExperimentalData("ASh-12", "12.7x55mm", "12.7x55mm STs-130", 285, "Lotte World Tower", 555, 9.8)
#Experiment(myData)

#Output Path
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "ExperimentalData.json")

#Data set of all the experimental data.
myDataSet = [ #Change the guns and other values. ExperimentalData stays the same.
    ExperimentalData("ASh-12", "12.7x55mm", "12.7x55mm STs-130", 285, "Lotte World Tower", 555, "Earth"),
    ExperimentalData("AK-104", "7.62x39mm", "7.62x39mm BP gzh", 730, "Lotte World Tower", 555, "Uranus"),
    ExperimentalData("AS VAL", "9x39mm", "9x39 mm SP5 gs", 290, "Lotte World Tower", 555, "Mars"),
    ExperimentalData("RPK-16", "5.45x39mm", "5.45x39mm PS gs", 890, "Lotte World Tower", 555, "Jupiter"),
    ExperimentalData("M1A", "7.62x51mm NATO", "7.62x51mm M80", 833, "Lotte World Tower", 555, "Neptune")
]
#ExperimentalData(myDataSet[0])

#Serialization 
with open(myOutputFilePath, "w") as outfile:
    json.dump(myData.__dict__, outfile)

with open(myOutputFilePath, "w") as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

Deserialize = open(myOutputFilePath,)
ExperimentJSON = json.load(Deserialize)

for e in ExperimentJSON:
    ExperimentalData(**e).Run()
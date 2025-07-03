import math
from pathlib import Path
import os
from ExperimentalData import ExperimentalData
import json

# Gun="OP-SKS"
# Caliber="7.62x39mm"
# Ammunition="MAI AP"
# Velocity_Ms=875
# Building="One World Trade Center"
# BuildingHeight_m=541.3
# gravity_Ms=9.81

#Here im calculating the time by plugging in the formula with the variables defined on top. But first, you need to import the function of the square root.
def ProjectileFunction(experimentalData:ExperimentalData):
    time_s = math.sqrt((2 * experimentalData.BuildingHeight_m) / experimentalData.gravity_Ms)
#Now that time is calculated, the variable is plugged into another formula to calculate distance, or delta x (Δx). 
    Distance_m = (experimentalData.Velocity_Ms * time_s)
    print(f"In this experiment, the distance of the projectile fired from a {experimentalData.Gun} was calculated in {experimentalData.planet}. The caliber of the gun was {experimentalData.Caliber} and the projectile fired is a(n) {experimentalData.Ammunition} with a speed of {experimentalData.Velocity_Ms}m/s. The building chosen for this experiment was the {experimentalData.Building} with a height of {experimentalData.BuildingHeight_m} meters. By using the formula for time, the time was {time_s} seconds. Then the time was plugged into another formula to calculate the distance, which was {Distance_m} meters\n")

# experimentalData ={
#     "Gun=" : "OP-SKS",
#     "Caliber" : "7.62x39mm",
#     "Ammunition" : "MAI AP",
#     "Velocity_Ms" : 875,
#     "Building=" : "One World Trade Center",
#     "BuildingHeight_m" : 541.3,
#     "gravity_Ms" : 9.81
# }

myDataset = [
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,3.7,"Mercury"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,8.87,"Venus"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,9.81,"Earth"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,3.711,"Mars"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,24.79,"Jupiter"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,10.44,"Saturn"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,8.69,"Uranus"),
    ExperimentalData("OP-SKS","7.62x39mm","MAI AP",875,"One World Trade Center",541.3,11.15,"Neptune"),
]
ProjectileFunction(myDataset[1])


myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath , "ExperimentalData.json")

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataset], outfile)

#This opens the Json file
deserialize = open(myOutputFilePath,)

#Here the data is deserialized
experimentJson = json.load(deserialize)

for e in experimentJson:
    ProjectileFunction(ExperimentalData(**e))
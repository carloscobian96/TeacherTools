import pathlib
from ExperimentData import ExperimentData
import json
import os
from pathlib import Path

# Gunname = ("Ak-101")
# Cartridgecalibre = ("5.56x45mm NATO")
# Round = ("5.56x45mm HP")
# Projectilespeed = 947
# Building = ("Lotte world tower")
# Buildingheight = 555
# gravity = 9.8

# def experiment(experimentData:ExperimentData):
#     time = (math.sqrt(2 * experimentData.Buildingheight/experimentData.gravity))
#     deltaX = (experimentData.Projectilespeed * time)

    # print(f"I shot a bullet from {experimentData.Building}, the height is {experimentData.Buldingheight}. It takes {time} to reach the ground if you are shooting from the top of the {experimentData.Building} because is {experimentData.Projectilespeed} fast and it have a distance of {deltaX}.")

# experimentData = {
#      "Gunname" : "Ak-101",
#      "Cartridgecalibre" : "5.56x45mm NATO",
#      "Round" : "5.56x45mm HP",
#      "Projectilespeed" : 947,
#      "Building" : "Lotte world tower",
#      "Buildingheight": 555 
#      "gravity" : 9.8 
# }

myDataSet = [
    ExperimentData("Ak-101", "5.56x45mm NATO", "5.56x45mm HP", 947, "Lotte world tower", 555, "Earth"),
    ExperimentData("Ak-103", "7.62x39mm", "7.62x39mm BP gzh", 730, "Lotte world tower", 555, "Mars"),
    ExperimentData("Ak-74N", "5.45x39mm", "5.45x39mm BP gs", 890, "Lotte world tower", 555, "Venus"),
    ExperimentData("AKM", "7.62x39mm", "7.62x39mm HP", 754, "Lotte world tower", 555, "Mercury"),
    ExperimentData("AKS-74UB", "5.45x39mm", "5.45x39mm BT gs", 880, "Lotte world tower", 555, "Neptune")
]

# experiment(myDataSet[0])

#Serealization

myOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(myOutputPath, 'ExperimentData.json')

with open(MyOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

#Deserialization
deserialize = open(MyOutputFilePath,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("-----------------------------------")
    ExperimentData(**e).run()
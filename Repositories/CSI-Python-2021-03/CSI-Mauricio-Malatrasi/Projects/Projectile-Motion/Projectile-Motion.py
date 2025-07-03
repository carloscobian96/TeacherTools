import os
from ExperimentData import ExperimentData
from pathlib import Path
import json

# Gunname = ("HK 416A5")
# Guncartridge = ("5.56x45mm NATO")
# Round = ("5.56x45mm HP")
# Roundvelocity = 947 #m/s
# Building = ("El Choli")
# Buildingheight = 48.5 #meters
# gravity = 9.8 #m/s


# def experiment(experimentData:ExperimentData):
    # Im calculating time and DeltaX.

    # time = (math.sqrt(2 * experimentData.Buildingheight/experimentData.gravity))
    # DeltaX = (experimentData.Roundvelocity * time)

    # print(f"I shot a projectile from {experimentData.Building}, it's {experimentData.Buildingheight} meters high. It goes at {experimentData.Roundvelocity} and it takes about {time} seconds to reach the ground. The distance covered is {DeltaX}.")


# experimentData = {
#     "Gunname" : "HK 416A5",
#     "Guncartridge" : "5.56x45mm NATO",
#     "Round" : "5.56x45mm HP",
#     "Roundvelocity" : 947,
#     "Building" : "El Choli",
#     "Buildingheight" : 48.5,
#     "gravity" : 9.8
# }

myDataSet = [
    ExperimentData("HK 416A5", "5.56x45mm NATO", "5.56x45mm HP", 947, "El Choli", 48.5, "Pluto"),
    ExperimentData("NSV Utes", "12.7x108mm", "12.7x108mm B-32 gl", 818, "El Choli", 48.5, "Venus"),
    ExperimentData("M1A", "7.62x51 mm NATO", "7.62x51 mm FMJ", 840, "El Choli", 48.5, "Earth"),
    ExperimentData("DVL-10", "7.62x51 mm NATO", "7.62x51 mm M61", 849, "El Choli", 48.5, "Mars"),
    ExperimentData("FN GL40", "40x46 mm", "40x46 mm M381 (HE) grenade", 76, "El Choli", 48.5, "Uranus")
]
# experiment(myDataSet[0])

#Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentData.json')

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

#Deserialization
deserialize = open(myOutputFilePath,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("-----------------------")
    ExperimentData(**e).run()
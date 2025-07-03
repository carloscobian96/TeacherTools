import os
from ExperimentData import ExperimentData
from pathlib import Path
import json


#gun = "AK-74"
    #cartridge = "5.45x39mm"
    #ammunition= "5.45x39mm PPBS gs"
    #velocity = 905
    #buildingName = "Minillas North Tower"
    #  #buildingHeight = 72.85

# def experiment(experimentData:ExperimentData):



    #Calculate the time that the bullet will fly for
    #time = (math.sqrt(2 * experimentData.buildingHeight)/9.8)
    #Calculate the distance the bullet will travel using the folloeing equation
    #distance =  experimentData.velocity*time
    # print(f"The weapon i choose was {experimentData.gun} and the cartridge of the gun is {experimentData.cartridge}. This cartridge has this type of ammunition {experimentData.ammunition}, the velocity of this ammunition is {experimentData.velocity}m/s. The building I choose was {experimentData.buildingName} and it has a height of {experimentData.buildingHeight}m. The bullet will travel for this much time {time} and for this distance {distance}. There is no air resistance therefore it wont affect the time and distance it will travel.")


# experimentData = {
#  "gun" : "AK-74",
#  "cartridge" : "5.45x39mm",
#  "ammunition": "5.45x39mm PPBS gs",
#  "velocity" : 905,
#  "buildingName" : "Minillas North Tower",
#  "buildingHeight" : 72.85
#  }

myDataSet =[

    ExperimentData("AK-74", "5.45x39mm", "5.45x39mm PPBS gs", 905, "Minillas North Tower", 72.85, "Mars"),
    ExperimentData("MP5", "9x19mm Parabellum", "9x19mm PBP gzh", 560, "Minillas North Tower", 72.85, "Neptune"),
    ExperimentData("SKS", "7.62x39mm", "7.62x39mm BP gzh", 730, "Minillas North Tower", 72.85, "Earth"),
    ExperimentData("M4A1", "5.56x45mm NATO", "5.56x45mm FMJ", 957, "Minillas North Tower", 72.85, "Uranus"),  
    ExperimentData("SV-98", "7.62x54mmR", "7.62x54R BT gzh", 820, "Minillas North Tower", 72.85, "Mercury")
]

# experiment(myDataSet[1])

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentData.json')

with open(myOutputFilePath, 'w') as outfile:
   # json.dump(myDataSet[1], outfile)
   json.dump([data.__dict__ for data in myDataSet], outfile)


deserialize = open(myOutputFilePath,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("----------------------")
    ExperimentData(**e).run()

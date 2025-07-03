import math
import os
from ExperimentData import ExperimentData
import json 
from pathlib import Path

Gunname = ("DVL-10")
Cartridgecalibre = ("7.62x51mm NATO")
Round = ( "7.62x51mm M61")
Roundvelocity = 849

# I was searching for a sniperrifle that shoots far and chose this one

Building = ("Burj Khalifa")
Buildingheight = 555
gravity = 9.8

# I searched for the tallest building in the world and chose the Burj Khalifa

time = (math.sqrt(2 * ExperimentData.Buildingheight/ExperimentData.gravity))
DeltaX = (ExperimentData.Roundvelocity/time)

print(f"I shot a {Gunname} from {Building} and the {Buildingheight} meters high. It goes at {Roundvelocity} and it takes about{time} seconds to reach {DeltaX}.")

mydata = ExperimentData

# expirementData= { 
#     "Gunname" : "DVL-10",
# "Cartridgecalibre" : "7.62x51mm NATO",
# "Round" :  "7.62x51mm M61",
# "Roundvelocity" : 849,
# "Building" : "Burj Khalifa",
# "Buildingheight" : 555
# ,
# "gravity" : 9.8
# }

# n"Gunname" : "DVL-10",
# "Cartridgecalibre" : "7.62x51mm NATO",
# "Round" :  "7.62x51mm M61",
# "Roundvelocity" : 849,
# "Building" : "Burj Khalifa",
# "Buildingheight" : 555,
# "gravity" : 9.8
# }
print(ExperimentData["Gunname", "7.62k51mm NATO", "7.62x51mm M61","Burj Khalifa","555", "9.8"])
experiment:(mydata)

myDataSet = [
    ExperimentData("DVL-10", "7.62x51mm NATO", 849,"Burj Khalifa", "555", "Mercury"),
    ExperimentData("DVL-10", "7.62x51mm NATO", 849,"Burj Khalifa", "555", "Mars"),
    ExperimentData("DVL-10", "7.62x51mm NATO", 849,"Burj Khalifa", "555", "Jupiter"),
    ExperimentData("DVL-10", "7.62x51mm NATO", 849,"Burj Khalifa", "555", "Venus"),
    ExperimentData("DVL-10", "7.62x51mm NATO", 849,"Burj Khalifa", "555", "Earth"),
    
]
#Sereliazation

myOutpuPath = Path(__file__).parent[0]
myOutputFilePath = os.path.join(myOutpuPath, 'Projectile-Motion.json')

with open(myOutputFilePath,'w') as outfile:
    json.dump(mydata._dict_ for data in myDataSet ,outfile)

#Deserialization

deserialize = open(myOutpuPath,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("---------------------------")
    
    ExperimentData(**e).run()
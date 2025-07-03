import math
import os
import json
from ExperimentalData import ExperimentalData
from pathlib import Path

# gun= "mp5"
# CartridgeCalibre = "9x19mm Parabellum"
# ammunition = "9x19mm PBP gzh"
# ProjectileVelocity_mps= 560 
# building = "Oriental Plaza"
# buildingHeight_m = 64


# def experiment(experimentalData:ExperimentalData):
#    #Calculate the time the bullet will fly for#
#     # time_s = math.sqrt((2*experimentalData.buildingHeight_m)/experimentalData.gravity)
#     #Using the time and velocity,calculate how far it will travel#
#     distance_m = experimentalData.ProjectileVelocity_mps * time_s

    # print(f"We will shoot the {experimentalData.gun} from {experimentalData.building}, which is {experimentalData.buildingHeight_m}m high. The {experimentalData.gun}'s catridge calibre is {experimentalData.CartridgeCalibre} and it is using the {experimentalData.ammunition} bullets. The {experimentalData.gun} shoots at {experimentalData.ProjectileVelocity_mps} m/s, it took { round(time_s, 2) } seconds to hit the ground and it traveled {round(distance_m, 2) } meters.\n")


# experimentalData={
# "gun" : "mp5",
# "CartridgeCalibre" : "9x19mm Parabellum",
# "ammunition" : "9x19mm PBP gzh",
# "ProjectileVelocity_mps" : 560,
# "building" : "Oriental Plaza",
# "buildingHeight_m" : 64,
# "gravity": 9.8
# }
MyDataSet = [
    ExperimentalData("mp5", "9x19mm Parabellum","9x19mm PBP gzh",560,"Oriental Plaza", 64, "Jupiter"),
    ExperimentalData("M4A1", "5.56x45mm NATO","5.56x45mm FMJ",957,"Oriental Plaza", 64, "Saturn"),
    ExperimentalData("MCX", ".300 Blackout",".300 AAC Blackout AP",720,"Oriental Plaza", 64,"Neptune"),
    ExperimentalData("Mk47", "7.62x39mm","7.62x39mm BP gzh",730,"Oriental Plaza", 64,"Earth"),
    ExperimentalData("mp9", "9x19mm Parabellum","9x19mm Pst gzh",457,"Oriental Plaza", 64,"Mercury")

]

# experiment(MyDataSet[0])

#Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentalData.json') 

with open(myOutputFilePath, 'w') as outfile:
    # json.dump(MyDataSet[0].__dict__,outfile)
    json.dump([data.__dict__ for data in MyDataSet], outfile)

#Deserialization
deserialize = open(myOutputFilePath,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n----------------------------------------------\n")
    ExperimentalData(**e).run()
    

    # experiment(ExperimentalData(**e))

    # ExperimentalData(**e).run()
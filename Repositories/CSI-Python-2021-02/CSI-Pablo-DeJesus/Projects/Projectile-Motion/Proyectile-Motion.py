import math
from ExperimentData import ExperimentData

import os
from pathlib import Path

import json

    # Gun= "Glock18C"
    # Guncartridge="9x19mm Parrabellum"
    # Gunround="AP63"
    # v_ms= 467
    # Building= "Burj Khalifa"
    # h_m=829.8
    # gravity_ms=9.81
def ProjectileFunction(ExperimentData:ExperimentData):
    time_s=(math.sqrt(2*h_m/ExperimentData.gravity_ms))
    Deltax_m=(math(ExperimentData.v_ms*time))
    print(f"""Here im calculating the time by replacing the formula with the variables defined previously. But first, I imported the function of the square root.
     In this first part of the experiment, the distance of the projectile fired from a {ExperimentData.Gun} was calculated,The caliber of the gun was {ExperimentData.Guncartridge} and the projectile fired is a {ExperimentData.Gunround} with a speed of {ExperimentData.v_ms}N/s.
     The building chosen for this experiment was the {ExperimentData.Building} with a height of {ExperimentData.Building} height.m)meters.
     By using the formula for time, the time was {ExperimentData.time_s} seconds. The planet on the experiment will be described by {ExperimentData.gravity_ms}
    Then the time was replaced into another formula to calculate the distance, which was {ExperimentData.Deltax_m} meters"-»""")
    # * experimentalData=f
    # '"'Gun" : "Glock18C"
    # "Caliber" : "9x19mm Parrabellum"
    # "Ammunition" : "AP63"
    # '"Velocity Ms" : 467,
    # "Building" : "Burj Khalifa",
    # "h_m" : 829.8
    # "gravity_ms" : "9.81"

myDataSet = [
    ExperimentData("Glock18C","9x19" "MAI AP",875,"Burj Khalifa",541.3,3.7) ,
    ExperimentData("OP-SKS","7-62×39mm ","MAI AP",875, "One World Trade Center",530.2,9.81) ,
    ExperimentData("OP-SKS","7-62×39mm","MAI AP",875, "El Choli",541.3,9.81) ,
    ExperimentData("Glock 17","7-62×39mm","MAI AP",875, "One World Trade Center",541.3,4.2) ,
    ExperimentData("Glock18C","7-62×39mm","MAI AP",875, "Lotte World Tower",541.3,9.81) ]

ProjectileFunction(myDataSet[0])

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath,"ExperimentData,json")
# Serialization
# with open (myOutputFilePath,'W') as outfile:
#json.dump(myDataset[0].dict__ outfile)

with open (myOutputFilePath,'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)



# Desenialization
# Opening the JSON file
deserialize = open (myOutputFilePath,)

experimentJsom = json.load(deserialize)

for e in experimentJson:
    ExperimentData(e***)
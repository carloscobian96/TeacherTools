import math
from ExperimentData import ExperimentData

import os
from pathlib import Path

import json

# Gun="RPK-16"
# Guncartridge="5.45x39mm,"
# Gunround="5.45x39mm FMJ"
# v_ms=884
# Building="Burj Khalifa"
# h_m=829.8
# gravity_ms=9.81

#Here I made a function that contains both the time_s and DeltaX_m variables, as well as my paragraph explaining my purpose in this experiment.
def ProjectileFunction(experimentData:ExperimentData):
    time_s= (math.sqrt(2*experimentData.h_m/experimentData.gravity_ms))
    DeltaX_m = (math(experimentData.v_ms*time_s))
    print(f"""In this experiment, I will be using {experimentData.Gun} from the game "Escape from Tarkov". I will also use both {experimentData.Guncartridge} and {experimentData.Gunround} of my choice. The velocity of the cartridge is {experimentData.v_ms}. The velocity is important because I want to see how far my projectile would go if fired at {experimentData.Building} using the cartridge with that set velocity. The height of the building, {experimentData.h_m}, is also important because the pull of gravity, {experimentData.gravity_ms}, will affect it the velocity and distance of the projectile the further it goes.""")

#Here I made it so that experimentData would have all of these variables as its value. I did this by using brackets that go from the top to the bottom of all the variables, which makes all of it part of ExperimentData.
#    experimentData = {
#    "Gun" : "RPK-16",
#    "Guncartridge" : "5.45x39mm,"
#    "Gunround" : "5.45x39mm FMJ"
#    "v_ms" : 884
#    "Building" : "Burj Khalifa"
#    "h_m" : 829.8
#    "gravity_ms" : 9.81
# }

#Here I am making a data set containing all the same variables except the buildings and the gravity/planets. This is so that I can have different sets of my ExperimentData that I can use to see how far the bullets I fire with the rest of variables go on different buildings that are on different planets.
myDataSet = [
    ExperimentData("RPK-16", "5.45x39mm", "5.45x39mm FMJ", 884, "Burj Khalifa", 829.8, 9.81),
    ExperimentData("RPK-16", "5.45x39mm", "5.45x39mm FMJ", 884, "Empire State Building", 443, 9.81),
    ExperimentData("RPK-16", "5.45x39mm", "5.45x39mm FMJ", 884, "Q1 Tower", 332.5, 9.81),
    ExperimentData("RPK-16", "5.45x39mm", "5.45x39mm FMJ", 884, "The Great Pyramid of Giza", 138, 9.81),
    ExperimentData("RPK-16", "5.45x39mm", "5.45x39mm FMJ", 884, "Eiffel Tower", 324, 9.81)
]

#Here I made a function to choose which data set I want to use. 
ProjectileFunction(myDataSet[0])

#Here I created an output file path using the os and ExperimentData.json. This is the process of serializing. 
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath , 'ExperimentData.json')

with open(myOutputFilePath, 'w') as outfile: 
    json.dump(myDataSet[0].__dict__ , outfile)


#In this part I will be deserializing myOutputFilePath and making a line of code to accomplish that task. 
deserialize = open(myOutputFilePath)

experimentJson = json.load(deserialize)

newList = []

for e in experimentJson:
    ExperimentData(**e).run()  

Gunnames= "RPK-16"
Guncartridges= "5.45x39mm,"
Gunrounds= "5.45x39mm FMJ"
v_ms= 884
Building= "Burj Khalifa"
h_m= 829.8

time= (math.sqrt(2*experimentData.Buildingheight/experimentData.gravity))
DeltaX = (math(experimentData.v_ms(experimentData.time)))

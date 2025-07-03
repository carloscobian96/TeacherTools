# First, you must import math in order to use square roots in the formula for Time. 
# It will be useful for determining the projectile's final velocity.
# Importing ExperimentData will allow for the creation of a .json file using the data from ExperimentData.py


import math
from ExperimentData import ExperimentData

import os
from pathlib import Path

import json

# These are the initial parameters I put for the projectile's function:

# ProjectileGun= "PB Pistol"
# ProjectileCartridge = "9x18mm PM PPe gzh"
# InitialVelocity = 297
# ProjectileWeight = 0.009
# BuildingLocation= "AdventureLand"
# BuildingHeight = 70
# G= 9.8

# In order to set the parameters, first you must define time and the final velocity, which require a mathematical equation like the ones put below
# You may notice that the parameters have 'experimentData' before them. 
# This is so that they are listed in the .json file as a class.

 # def ProjectileFunction(experimentData: ExperimentData):
# Time = math.sqrt((ExperimentData.BuildingHeight * 2) / ExperimentData.getGravity())
# Distance = (ExperimentData.getTime * ExperimentData.Velocity)

# After this, you'll need to lay out a conclusion using the given information. 
# It is important that you lay the parameters like this so that they can be altered later on.

# print(f"For the purpose of this experiment, I shot a {ExperimentData.ProjectileCartridge} bullet from a {ExperimentData.ProjectileGun} from the roof of {ExperimentData.BuildingLocation} to determine the final velocity of a projectile.")
# print(f"It was under the gravitational acceleration of {ExperimentData.getGravity()} m/s^2.")
# print(f"It also held a velocity of {ExperimentData.Velocity} meters per second and was shot from a height of {ExperimentData.BuildingHeight} meters.")
# print(f"Using these variables, I calculated the final velocity of the bullet by first finding the time it took to land, which was {ExperimentData.getTime} seconds.")
# print(f"After this, I gathered the time and multiplied it with the initial velocity, to find that the projectile had a final velocity of {ExperimentData.getDistance} m/s.")
# print(f"In conclusion, I was able to determine the final velocity of my {ExperimentData.ProjectileGun}'s projectile by gathering its given values to first find the estimated time it would take to land, and then apply it to its initial velocity.\n")

# myExperiment("PB Pistol","9x18mm PM PPe gzh",297,0.009,"AdventureLand",70,9.81)

# experimentalData = {
#    "ProjectileGun" : "PB Pistol"
#    "ProjectileCartridge" : "9x18mm PM PPe gzh"
#    "InitialVelocity" : 297
#    "ProjectileWeight" : 0.009
#    "BuildingLocation" : "AdventureLand"
#    "BuildingHeight" : 70
#    "Planet" : 9.81
#}

# Now, with this data set, you utilize the given parameters and lay them out in this list.
# This way, you can alter the specific values in this projectile.

myDataSet = [
ExperimentData("PB Pistol", "9x18mm PM PPe gzh",297, "AdventureLand", 70, "Earth"),
ExperimentData("PPSh-41 submachine gun", "7.62x25mm TT AKBS",425, "Carribean Sea View", 102,"Mercury"),
ExperimentData("Mosin bolt-action sniper rifle", "7.62x54mm R BS",785, "Soleil", 88, "Venus"),
ExperimentData("FN40GL Mk2 grenade launcher", "40x46mm M441 (HE)",76, "Torre Norte", 74, "Jupiter"),
ExperimentData("PB Pistol", "9x18mm PM PSO gzh",315, "Oriental Plaza", 64, "Neptune")
]

#Each parameter contains the weapon, the bullet and its speed, weight, height, and gravity.

# ProjectileFunction(myDataSet[0])

# Then you'll need to activate the .json file to make a class.

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentData.json')

# Serialization
#  with open(myOutputFilePath, 'w') as outfile:
#    json.dump([data.__dict__ for data in myDataSet], outfile)

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)


# Deserialization:
# Opening the JSON File
deserialize = open(myOutputFilePath)

# Deserializing the data
experimentJson = json.load(deserialize)

newList = []

for e in experimentJson:
    ExperimentData(**e).run()
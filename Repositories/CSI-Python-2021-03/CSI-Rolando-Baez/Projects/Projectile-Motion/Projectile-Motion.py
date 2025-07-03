import os
from ExperimentalData import ExperimentalData
from pathlib import Path
import json
#Gives values to the ExperimentalData variables
myDataSet = [
    ExperimentalData("SV-98", "7.62x54R", "7.62x54R BS", 785, "Willis Tower", 526.99, "Earth")][
    ExperimentalData("SV-98", "7.62x54R", "7.62x54R BS", 785, "Willis Tower", 526.99, "Mars") ][
    ExperimentalData("SV-98", "7.62x54R", "7.62x54R BS", 785, "Willis Tower", 526.99, "Venus") ][
    ExperimentalData("SV-98", "7.62x54R", "7.62x54R BS", 785, "Willis Tower", 526.99, "Saturn") ][
    ExperimentalData("SV-98", "7.62x54R", "7.62x54R BS", 785, "Willis Tower", 526.99, "Mercury") ]


# | This code looks to calculate how far a "BS" bullet shot from an SV-98 while on-top of the Willis Tower travels. The projectile speed
# | of the bullet is 785 m/s while the height of the building is 526.99m. To find the distance the bullet travels we need to find time
# | it travels the formula needed to use to find this is (((2*height)/gravity) ** 0.5) after finding the time it travels for we can 
# | find the distance by using this formula (speed*time).

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

with open(myOutputFilePath, 'w') as outfile:
     json.dump([data.__dict__ for data in myDataSet], outfile)

# deserialization
deserialize = open(myOutputFilePath,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    ExperimentalData(**e)


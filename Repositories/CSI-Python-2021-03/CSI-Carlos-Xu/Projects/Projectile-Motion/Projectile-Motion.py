import math
import os
from ExperimentalData import ExperimentData

from pathlib import Path
import json

# gun = "AK-101"
# caliber = "5.56 x 45mm"
# ammunition = "FMJ"
# velocity_ms = 957

# Building = "Ocean Tower"
# BuildingHeight = 243

# gravity_ms = 9.81

# def experiment (experimentalData:ExperimentData):
def ProjectileFunction(experiementalData:ExperimentData):

# Calculating the time the bullet will fly for
    time_s = math.sqrt((2 * experiementalData.BuildingHeight) / experiementalData.gravity_ms)

# Using time and velocity, I'm going to calculate how far will the bullet travel
    distance = (experiementalData.velocity_ms * time_s)

# Function to print the descriptive paragraph of the experiment.
    print(f"The gun selected for the experiment is {experiementalData.gun}. The caliber of {experiementalData.gun} is {experiementalData.caliber}. Its ammunition is {experiementalData.ammunition}. I will launch the projectile from {experiementalData.Building} from a {experiementalData.BuildingHeight}. ")
    print(f"The ammunition has a velocity of {experiementalData.velocity_ms}. The projectile will travel a certain amount of {distance} in {time_s} below a gravity of {experiementalData.gravity_ms}")


#experimentalData = ExperimentData("AK-101","5.56 x 45mm","FMJ",957,"Ocean Tower",243,9.81)

# assign values to each parameter from de class containing the datatype: ExperimentData
myDataSet = [
ExperimentData("AK-101","5.56 x 45mm","FMJ",957,"Ocean Tower",243,9.81),
ExperimentData("AK-101","5.56 x 45mm","FMJ",957,"Soleil",288,9.81),
ExperimentData("AK-101","5.56 x 45mm","FMJ",957,"Popular Center",247,9.81),
ExperimentData("AK-101","5.56 x 45mm","FMJ",957,"Torre Norte",243,9.81),
ExperimentData("AK-101","5.56 x 45mm","FMJ",957,"Oriental Plaza",210,9.81)

]
# for-loop
for data in myDataSet:
    print("\n--------------------------------------\n")
    ProjectileFunction(data)

# Serialization means to convert an object into a string representing an object
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

with open(myOutputFilePath, 'w') as outfile:
# json.dump serializes an object into a file. It takes 2 parameters, the object and the destination file.
    json.dump([data.__dict__ for data in myDataSet], outfile)


import math
import os
from ExperimentData import ExperimentData
from pathlib import Path
import json

# Here i defined the variables
# gun = "APB"
# cartridge = "9x18mm"
# bullet = "9x18mm PM BZhT gzh"
# velocity = 325
# buildingName = "Birj Khalifa"
# buildingHeight = 828

# Here i told the program to use the variables i just defined , specifically: velocity and building height, to use math to find out the time the bullet wil travel, to then find the distance the bulllet will travel, considering there is no air resistance.
# time = math.sqrt((2*buildingHeight)/9.8)
# distance = velocity * time

# Here i made a descriptive paragrapgh describing the experiment using the variables and the results from the previous equation.
# print(f"In this experiment, we are climbing {buildingHeight} meters to the top of {buildingName} and shooting a {gun} with a cartidge of {cartridge} using a {bullet}. Considering there is no air resistance, the bullet will travel with a velocity of {velocity}m/s and a distance of {distance}meters ")

# def calculateBulletDT(experimentData: ExperimentData):
    # time = math.sqrt(2*experimentData.buildingHeight / experimentData.gravity)
    # distance = experimentData.velocity * time

# experimentalData = {"gun" : "APB"
# "cartridge" : "9x18mm"
# "bullet" : "9x18mm PM BZhT gzh"
# "velocity" : 325
# "buildingName" : "Birj Khalifa"
# "buildingHeight" : 828}

    # print(f"In this experiment, we are climbing {experimentData.buildingHeight} meters to the top of {experimentData.buildingName} and shooting a {experimentData.gun} with a cartidge of {experimentData.cartridge} using a {experimentData.bullet}. Considering there is no air resistance, the bullet will travel with a velocity of {experimentData.velocity}m/s and a distance of {distance}meters ")

# calculateBulletDT("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00)

# Here im defining my data set with all the parameters
myDataSet = [

ExperimentData("APB", "9x18mm", "9x18mm PM BZhT gzh", 325.00, "Birj Khalifa", 828.00, "Mercury"),
ExperimentData("SKS", "7.62x39mm", "7.62x39mm PS gzh", 700.00, "Birj Khalifa", 828.00, "Saturn"),
ExperimentData("MP5", "9x19mm Parabellum", "9x19mm Pst gzh", 457.00, "Birj Khalifa", 828.00, "Jupiter"),
ExperimentData("DVL-10", "7.62x51mm NATO", "7.62x51mm M80", 833.00, "Birj Khalifa", 828.00, "Venus"),
ExperimentData("FN GL40", "40x46 mm", "40x46mm M381(HE) grenade", 76.00, "Birj Khalifa", 828.00, "Mars")
]

# calculateBulletDT(myDataSet[0])

# Im definign the file using output path, then the output path joins the eperiment data
myOutputPath = Path(__file__) . parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'ExperimentData.json')

# Im taking my OutputFilePath and defining it as outfile so that it can read myDataSet
with open (myOutputFilePath, 'w') as outfile:
    # json.dump(myDatSet[0], outfile)
    json.dump([data.__dict__ for data in myDataSet], outfile)
    
# This is making the variable deserialize open myOutputFilePath and then loding the dataset with experimentJson.
deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)
# This is customizing the output
for e in experimentJson:
    print("\n------------------------------------\n")
    ExperimentData(**e).run()

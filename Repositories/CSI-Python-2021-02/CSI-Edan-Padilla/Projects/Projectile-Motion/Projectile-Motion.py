import json 
import os
from pathlib import Path
from ExperimentalData import ExperimentData

#Gun = "PPSh-41 7.62x25"
#Bullet = "7.62x25mm TT P gl"
#Caliber = "7.62x25mm Tokarev"
#Building = "Eifel Tower"
#BuildingHeight = "300 m"
#BulletSpeed = "430"
#BulletWeight = "0.01 kg"
#Gravity = 9.8

#print(f" In this experimetn i will be shooting a un from a building. The gun that I used was {Gun}. TZhe bullet that I used was {Bullet} and the calliber of the gun is {Caliber}. The building is {Building} and the height of the building is {BuildingHeight}. The bullet has a speed of {BulletSpeed}. The weight of the bullet is {BulletWeight}. The world was a gravity of {Gravity}.")

#t = math.sqrt(BuildingHeight)* 2/Gravity
#def ("Time")
#delta_X=math.sqrt(ProjectileDistance*t)

MyDataSet = [
    ExperimentData(f"MP7A1 4.6x30","9x19mm Parabellum", "9x19mm Pst gzh", 457, "Empire State", 457, "Mercury"),
    ExperimentData(f"MP9 9x19","9x19mm Parabellum","9x19mm Pst gzh", 457,"Central Park", 472,"Saturn"),
    ExperimentData(f"P90 5.7x28","5.7x28mm FN","5.7x28mm SS190",716, "Chrysler Building", 319, "Jupiter"),
    ExperimentData(f"UMP .45 ACP","45 ACP","45 ACP Match FMJ",285,"One World Trade Center",541,"Mars" ),
    ExperimentData(f"STM-9 Gen.2 9x19","9x19mm Parabellum","9x19mm Pst gzh", 457,"Woolworth Building", 241, "Earth")
]

MyOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(MyOutputPath,"Projectile-Motion.json")
with open(MyOutputFilePath,"w") as outfile:
    json.dump([data.__dict__ for data in MyDataSet],outfile)

deserialize = open(MyOutputFilePath)
ProjectileMotionjson = json.load(deserialize)

for e in ProjectileMotionjson:
        ExperimentData(**e).ToString()
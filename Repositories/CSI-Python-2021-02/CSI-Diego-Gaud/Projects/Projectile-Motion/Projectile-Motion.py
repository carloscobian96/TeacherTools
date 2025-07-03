import math
import os
import pathlib
import json
from ExperimentalData import Pylance
Gun = "HK416A5"
Cartridge = "5.56x45mm NATO"
Ammo = "5.56x45mm Warmageddon"
ProjectileDistance = 910
Building = "Tour Eiffel"
BuildingHeight = 324
Gravity = -9.8
print("Calculate")
t =math.sqrt(BuildingHeight)* 2/Gravity
delta_X=math.sqrt(ProjectileDistance*t)
print(f"In this experiment we would be testing shooting a spesific weapon from a the top of a building. We have the {Gun} with this {Cartridge} with this {Ammo} which has a distance of {ProjectileDistance} which will be shot from the top of the {Building} which is this tall {BuildingHeight}.{delta_X}is the displacement of the bullet from the origin point. {t} Is representative of time and thus how long it would take for the bullet to travel. All of this will show the result of these conditions if they were to take place in real life")
myDataSet=""
class ExperimentalData:
    def __init__(self,Gun ,Cartridge ,Ammo ,ProjectileDistance ,Building ,BuildingHeight ,Gravity ):
        self.Gun = Gun
        self.Cartridge = Cartridge
        self.Ammo = Ammo
        self.ProjectileDistance = ProjectileDistance
        self.Building = Building
        self.BuildingHeight = BuildingHeight
        self.Gravity = Gravity



# def ProjectileFunction 
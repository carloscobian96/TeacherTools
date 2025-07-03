import os

from ExperimentData import ExperimentData

from pathlib import Path

import json

# Gunname = "Knight's Armament Company SR-25"
# Guncartridge = "7.62x51mm NATO"
# Round = "7.62x51mm M993"
# RoundVelocity_ms = 910 
# Building = "Central Park Tower"
# BuildingHeight_m = 472
# Gravity_ms= 9.8

    
# experimentalData = {
#  "Gunname" : "Knight's Armament Company SR-25",
#  "Guncartridge" : "7.62x51mm NATO",
#  "Round" : "7.62x51mm M993",
#  "RoundVelocity_ms" : 910,
#  "Building" : "Central Park Tower",
#  "BuildingHeight_m" : 472,
#  "Gravity_ms": 9.8
# }

myDataSet = [
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm M993", 910, "Central Park Tower", 472, "Earth"),
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm M61", 849, "One World Trade Center", 472, "Mercury"),
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm FMJ", 840, "Central Park Tower", 472, "Venus"),
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm M80", 833, "One World Trade Center", 472, "Mars"),
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Central Park Tower", 472, "Saturn"),
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm M993", 910, "Central Park Tower", 472, "Uranus"),
     ExperimentData("Knight's Armament Company SR-25", "7.62x51mm NATO", "7.62x51mm M61", 849, "One World Trade Center", 472, "Neptune"),
]

# This code creates the JSON file 
MyOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(MyOutputPath , 'ExperimentData.json')

# This code calls the dictionary and sends the ExperimentData to the JSON file
with open(MyOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)


# Deserialization
# Opening the JSON file
deserialize = open(MyOutputFilePath,)

# Deserializing the data
experimentJson = json.load(deserialize)

# Reads the file and converts it back to the python
for e in experimentJson:
    ExperimentData(**e).run()







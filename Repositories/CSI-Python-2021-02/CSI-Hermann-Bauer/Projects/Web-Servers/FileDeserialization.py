import json
import os
from pathlib import Path
from Beer import Beer
import http

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_beer.json')
data = open(myFilePath, 'r')
 
# deserializing the data
data = json.load(data)
beer:Beer = Beer(**data)

# Print data from the object
print(f"ID: {beer.id}")
print(f"UID: {beer.uid}")
print(f"Brand: {beer.brand}")
print(f"Name: {beer.name}")
print(f"Style: {beer.style}")
print(f"Hop: {beer.hop}")
print(f"Yeast: {beer.yeast}")
print(f"Malts: {beer.malts}")
print(f"Ibu: {beer.ibu}")
print(f"Alcohol: {beer.alcohol}")
print(f"Blg: {beer.blg}")


import json
import os
from pathlib import Path
from RandomBeer import RandomBeer

myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_beer.json')
data = open(myFilePath,)

data = json.load(data)
beer:RandomBeer = RandomBeer(**data)

print(f"ID: {beer.id}")
print(f"UID: {beer.uid}")
print(f"Brand: {beer.brand}")
print(f"Name: {beer.name}")
print(f"Style: {beer.style}")
print(f"Hop: {beer.hop}")
print(f"Yeast: {beer.yeast}")
print(f"Malts: {beer.malts}")
print(f"IBU: {beer.ibu}")
print(f"Alcohol: {beer.alcohol}")
print(f"BLG: {beer.blg}")
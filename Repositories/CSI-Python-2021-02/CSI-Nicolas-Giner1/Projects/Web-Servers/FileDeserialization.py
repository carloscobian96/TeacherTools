from http.client import responses
from importlib.resources import path

# Importing json will be important (g-get it) to import and later deserialize the class file
import json

import os
from pathlib import Path
from Nation import Nation

# Loading and opening the json file so that it may be deserialized
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'nation.json')
data = open(myFilePath,)

# Defining the data to deserialize it
data= json.load(data)
nation:Nation = Nation(**data)

# Printing each variable from the list 
print(f"id: {nation.id}")
print(f"uid: {nation.uid}")
print(f"nationality: {nation.nationality}")
print(f"language: {nation.language}")
print(f"capital: {nation.capital}")
print(f"national sport: {nation.national_sport}")
print(f"flag: {nation.flag}")
print("Others expected...")
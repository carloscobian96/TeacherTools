import json
import os
from pathlib import Path
from Coffee import Coffee

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_coffee.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
coffee:Coffee = Coffee(**data)

# Print data from the object
print(f"id: {coffee.id}")
print(f"uid: {coffee.uid}")
print(f"blend_name: {coffee.blend_name}")
print(f"origin: {coffee.origin}")
print(f"variety: {coffee.variety}")
print(f"notes: {coffee.notes}")
print(f"intensifier: {coffee.intensifier}")

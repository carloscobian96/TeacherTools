import json
import os
from pathlib import Path
from RandomDessert import RandomDessert

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_dessert.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
dessert:RandomDessert = RandomDessert(**data)

# Print data from the object
print(f"ID: {dessert.id}")
print(f"UID: {dessert.uid}")
print(f"variety: {dessert.variety}")
print(f"topping: {dessert.topping}")
print(f"flavor: {dessert.flavor}")
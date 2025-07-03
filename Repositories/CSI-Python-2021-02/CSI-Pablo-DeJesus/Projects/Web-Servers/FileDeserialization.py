import json
import os
from pathlib import Path
from Food import Food

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_food.json')
data = open(myFilePath, 'r')
 
# deserializing the data
data = json.load(data)
food:Food = Food(**data)

# Print data from the object
print(f"ID: {food.id}")
print(f"UID: {food.uid}")
print(f"dish: {food.dish}")
print(f"description: {food.description}")
print(f"description: {food.description}")
print(f"ingredient: {food.ingredient}")
print(f"measurement: {food.measurement}")

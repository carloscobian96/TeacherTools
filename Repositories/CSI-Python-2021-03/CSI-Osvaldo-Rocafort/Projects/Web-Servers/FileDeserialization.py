import json
import os
from pathlib import Path
from Colors import Colors

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_colors.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
colors:Colors = Colors(**data)

# Print data from the object
print(f"ID: {colors.id}")
print(f"UID: {colors.uid}")
print(f"hex_value: {colors.hex_value}")
print(f"color_name: {colors.color_name}")
print(f"hsl_value: {colors.hsl_value}")
print(f"hsla_value: {colors.hsla_value}")
print("Others expected...")
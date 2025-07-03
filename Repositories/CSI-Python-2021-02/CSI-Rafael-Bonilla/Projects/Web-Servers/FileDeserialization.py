import json
import os
from pathlib import Path
from Color import Color

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_color.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
color:Color = Color(**data)

# Print data from the object
print(f"ID: {color.id}")
print(f"UID: {color.uid}")
print(f"Hex Value: {color.hex_value}")
print(f"Color Name: {color.color_name}")
print(f"hsl value: {color.hsl_value}")
print(f"hsla value: {color.hsla_value}")
print("Others expected...")
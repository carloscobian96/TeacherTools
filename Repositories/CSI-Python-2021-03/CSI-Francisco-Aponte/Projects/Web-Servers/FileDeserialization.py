import json
import os
from pathlib import Path
from RandomApp import RandomApp

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'Random_app.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
app:RandomApp = RandomApp(**data)

# Print data from the object
print(f"ID: {app.id}")
print(f"UID: {app.uid}")
print(f"app_name: {app.app_name}")
print(f"app_author: {app.app_author}")
print(f"app_semantic_version: {app.app_semantic_version}")
print(f"app_major_version: {app.app_major_version}")
print(f"app_minor_version: {app.app_minor_version}")
print(f"app_patch_version: {app.app_patch_version}")


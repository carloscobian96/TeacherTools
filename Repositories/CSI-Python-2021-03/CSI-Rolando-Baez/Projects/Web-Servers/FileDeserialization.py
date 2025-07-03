from http.client import responses
import json
import os
from pathlib import Path
from urllib import response
from RandomBlood import RandomBlood

myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'randomBlood.json')
data = open(myFilePath,)

data = json.load(data)
blood:RandomBlood = RandomBlood(**data)

print(f"ID: {blood.id}")  
print(f"UID: {blood.uid}")
print(f"Type: {blood.type}")
print(f"RH Factor: {blood.rh_factor}")
print(f"Group: {blood.group}")

bloodList = []
for blood in data:
    bloodList.append(RandomBlood(**blood))
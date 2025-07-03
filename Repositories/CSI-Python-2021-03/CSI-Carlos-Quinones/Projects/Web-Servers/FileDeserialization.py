import json
import os
from pathlib import Path
from RandomHipsterStuff import RandomHipsterStuff

myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_hipster_stuff.json')
data = open(myFilePath,)
 
data = json.load(data)

hipVariable:RandomHipsterStuff = RandomHipsterStuff(**data)


print(f"ID: {hipVariable.id}")
#print(f"UID: {hipVariable.uid}")

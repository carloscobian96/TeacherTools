import json
import os
from pathlib import Path
from Cannabis import Cannabis

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_cannabis.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
cannabis:Cannabis = Cannabis(**data)

# Print data from the object
print(f"ID: {cannabis.id}")
print(f"UID: {cannabis.uid}")
print(f"strain: {cannabis.strain}")
print(f"cannabinoid_abbreviation: {cannabis.cannabinoid_abbreviation}")
print("cannabinoid: {cannabis.cannabinoid}")
print(f"terpene: {cannabis.terpene}")
print(f"medical_use: {cannabis.medical_use}")
print(f"health_benefit: {cannabis.health_benefit}")
print(f"category: {cannabis.category}")
print(f"type: {cannabis.type}")
print(f"buzzword: {cannabis.buzzword}")
print(f"brand: {cannabis.brand}")

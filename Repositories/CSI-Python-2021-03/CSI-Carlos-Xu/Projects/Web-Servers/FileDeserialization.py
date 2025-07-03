import json
import os
from pathlib import Path
from RandomPhoneNumber import RandomPhoneNumber

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_phone_number.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
phonenumber:RandomPhoneNumber = RandomPhoneNumber(**data)

# Print data from the object
print(f"ID: {phonenumber.id}")
print(f"UID: {phonenumber.uid}")
print(f"phone_number: {phonenumber.phone_number}")
print(f"cell_phone: {phonenumber.cell_phone}")
print(f"cell_phone_in4_e164: {phonenumber.cell_phone_in_e164}")



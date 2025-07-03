import json
import os
from pathlib import Path
from Name import Name

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_name.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
name:Name = Name(**data)

# Print data from the object
print(f"ID: {name.id}")
print(f"UID: {name.uid}")
print(f"Name: {name.name}")
print(f"two_word_name: {name.two_word_name}")
print(f"four_word_name: {name.four_word_name}")
print(f"name_with_initials: {name.name_with_initials}")
print(f"name_with_middle: {name.name_with_middle}")
print(f"first_name: {name.first_name}")
print(f"middle_name: {name.middle_name}")
print(f"last_name: {name.last_name}")
print(f"male_first_name: {name.male_first_name}")
print(f"female_first_name: {name.female_first_name}")
print(f"prefix: {name.prefix}")
print(f"initials: {name.initials}")
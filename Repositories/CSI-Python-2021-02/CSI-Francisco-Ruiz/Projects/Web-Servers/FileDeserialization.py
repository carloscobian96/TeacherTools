import json
import os
from pathlib import Path
from InternetStuff import InternetStuff

#In this part of the code, I locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_internet_stuff.json')
data = open(myFilePath,)

#This part serves to deserialize the data
data = json.load(data)
internetstuff:InternetStuff = InternetStuff(**data)

#Here I am simply printing the data from the object
print(f"id: {internetstuff.id}")
print(f"uid: {internetstuff.uid}")
print(f"email: {internetstuff.email}")
print(f"username: {internetstuff.username}")
print(f"password: {internetstuff.password}")
print(f"domain_name: {internetstuff.domain_name}")
print(f"ip_v4_address: {internetstuff.ip_v4_address}")
print(f"private_ip_v4_address: {internetstuff.private_ip_v4_address}")
print(f"public_ip_v4_address: {internetstuff.public_ip_v4_address}")
print(f"ip_v4_cidr: {internetstuff.ip_v4_cidr}")
print(f"ip_v6_address: {internetstuff.ip_v6_address}")
print(f"ip_v6_cidr: {internetstuff.ip_v6_cidr}")
print(f"mac_address: {internetstuff.mac_address}")
print(f"url: {internetstuff.url}")
print(f"slug: {internetstuff.slug}")
print(f"user_agent: {internetstuff.user_agent}")
print("Others expected...")
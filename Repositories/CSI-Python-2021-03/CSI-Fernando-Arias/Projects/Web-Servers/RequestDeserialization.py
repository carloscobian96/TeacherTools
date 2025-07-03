import json, ssl
import urllib.request
from RandomDessert import RandomDessert
import os
from pathlib import Path

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
dessertURL = "https://random-data-api.com/api/dessert/random_dessert?size=100"

# Create a list to populate with our data
desserts:RandomDessert = [] 

myOutputPath = Path(__file__) .parents[0]

# Execute HTTP Request
req = urllib.request.Request(dessertURL)
requestData = json.loads(urllib.request.urlopen(req).read())

myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'responses')
os.mkdir(myFilePath,0o777)

for x in range(0,100):
        req = urllib.request.Request(dessertURL)
        requestData = json.loads(urllib.request.urlopen(req).read())

#Loop over JSON items and Deserialize them into python objects
        for r in requestData:
                #Deserialize
                dessert:RandomDessert = RandomDessert(**r)
                #Add object to list
                desserts.append(dessert)
                #Print id
                print(dessert.id)
                myOutputFilePath = os.path.join(myFilePath, f"{dessert.uid}.json")

                with open(myOutputFilePath, 'w') as outfile:
                        json.dump(dessert.__dict__, outfile)


from http.client import responses
import json, ssl
import os
from pathlib import Path
import urllib.request
from Coffee import Coffee

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
CoffeeURL = "https://random-data-api.com/api/coffee/random_coffee?size=100"

# Create a list to populate with our data
coffees:Coffee = [] 

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "responses")
os.mkdir(myOutputFilePath)

for x in range(100):

    # Execute HTTP Request
    req = urllib.request.Request(CoffeeURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        # Deserialize 
        coffee:Coffee = Coffee(**r)
        # Add object to list
        coffees.append(coffee) 
        # Print id
        print(coffee.id)

        filePath = os.path.join(myOutputPath, f"{coffee.uid}.json")

        with open(filePath, 'w') as outfile:
            json.dump(coffee.__dict__, outfile)
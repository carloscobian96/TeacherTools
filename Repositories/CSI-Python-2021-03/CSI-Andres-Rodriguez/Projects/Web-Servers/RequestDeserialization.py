import json, ssl
import os
from pathlib import Path
import urllib.request
from Cannabis import Cannabis

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cannabisURL = "https://random-data-api.com/api/cannabis/random_cannabis?size=100"

# Create a list to populate with our data
cannabises:Cannabis = [] 

# Execute HTTP Request
# req = urllib.request.Request(cannabisURL)
# requestData = json.loads(urllib.request.urlopen(req).read())

# # Loop over JSON items and Deserialize them into python objects
# for r in requestData:  
#     # Deserialize 
#     cannabis:Cannabis = Cannabis(**r)
#     # Add object to list
#     cannabises.append(cannabis) 
#     # Print id
#     print(cannabis.strain)

myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')

os.mkdir(myFolderPath)

for x in range(0,100):
    req = urllib.request.Request(cannabisURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    
    for r in requestData:  
        # Deserialize 
        cannabis:Cannabis = Cannabis(**r)
        # Add object to list
        cannabises.append(cannabis) 
        # Print id
        print(cannabis.strain)
        myFilePath = os.path.join(myFolderPath, f"{cannabis.uid}.json")

        with open(myFilePath, 'w') as outfile:
            json.dump(cannabis.__dict__, outfile)
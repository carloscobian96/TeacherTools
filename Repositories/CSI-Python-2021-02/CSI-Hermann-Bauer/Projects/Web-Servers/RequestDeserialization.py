
import json, ssl
import urllib.request
from Beer import Beer
import json
import os
from pathlib import Path

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context
#Make folder for requests named responses
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.makedirs(myFolderPath)

# This is the URL from which we will request the data
beerURL = "https://random-data-api.com/api/beer/random_beer?size=100"

# Create a list to populate with our data
beers:Beer = [] 

# Loop over JSON items and Deserialize them into python objects
for i in range(100):
    #make the request
    req = urllib.request.Request(beerURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    for r in requestData:  
        # Deserialize 
        current_beer:Beer = Beer(**r)
        # Add object to list
        beers.append(current_beer) 
        # Print id
        print(current_beer.name)
        #Create new file using uid as name and dump json
        myFilePath = os.path.join(myFolderPath, f"{current_beer.uid}.json")
        with open(myFilePath, 'w') as outfile:
            json.dump(current_beer.__dict__, outfile)


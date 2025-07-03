import json, ssl
import urllib.request
import os
from pathlib import Path
from Name import Name

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
nameURL = "https://random-data-api.com/api/name/random_name?size=100"

# Create a list to populate with our data
names:Name = [] 

myOutputPath = Path(__file__).parents[0]


# Execute HTTP Request
req = urllib.request.Request(nameURL)
requestData = json.loads(urllib.request.urlopen(req).read())


myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'responses')
os.mkdir(myFilePath,0o777)


for x in range (0,100):
    req = urllib.request.Request(nameURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        # Deserialize 
        name:Name = Name(**r)
        # Add object to list
        names.append(name) 
        # Print id
        print(name.id)

        myOutputFilePath = os.path.join(myFilePath, f"{name.uid}.json")
    
        with open(myOutputFilePath,"w") as outfile:
            json.dump(name.__dict__, outfile)


import json, ssl
import os
import json
from pathlib import Path
import urllib.request
from Name import Name

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# Make folder for requests named response
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'response')
os.makedirs(myFolderPath)

# This is the URL from which we will request the data
nameURL = "https://random-data-api.com/api/name/random_name?size=100"

# Create a list to populate with our data
names:Name = [] 

# Loop over JSON items and Deserialize them into python objects
for i in range(100):

    # make the request
    req = urllib.request.Request(nameURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    for r in requestData:  
        # Deserialize 
        current_name = Name(**r)

        # Add object to list
        names.append(current_name) 

        # Print id
        print(current_name.id)
        
        #Create new file using uid as name and dump json
        myFilePath = os.path.join(myFolderPath, f"{current_name.uid}.json")

        with open(myFilePath, 'w') as outfile:
            json.dump(current_name.__dict__, outfile)
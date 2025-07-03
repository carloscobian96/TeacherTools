import json, ssl
import os
from pathlib import Path
import urllib.request
from Colors import Colors

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
colorsURL = "https://random-data-api.com/api/color/random_color?size=100"

#Locate and open file
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.mkdir(myFolderPath)

# Create a list to populate with our data
colors:Colors = [] 

for x in range(100):
    

    # Execute HTTP Request
    req = urllib.request.Request(colorsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        # Deserialize 
        color:Colors = Colors(**r)
        # Add object to list
        colors.append(color) 
        # Print id
        print(color.id)
        
        myOutputFilePath = os.path.join(myFolderPath,f"{color.uid}.json")
        with open(myOutputFilePath,'w') as outfile:
            json.dump(color.__dict__,outfile)
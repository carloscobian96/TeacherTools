from http.client import responses
import json, ssl
import urllib.request
import os
from pathlib import Path
from RandomApp import RandomApp

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
appURL = "https://random-data-api.com/api/app/random_app?size=100"

# Create a list to populate with our data
apps:RandomApp = [] 

myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
data = os.mkdir(myFolderPath,)

for x in range (0,100):
    # Execute HTTP Request
    req = urllib.request.Request(appURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        # Deserialize 
        app:RandomApp = RandomApp(**r)
        # Add object to list
        apps.append(app) 
        # Print id
        print(app.id)
        myFilePath = os.path.join(myFolderPath, f"{app.uid}.json")

        with open (myFilePath, 'w') as outfile:
            json.dump(app.__dict__, outfile)
    


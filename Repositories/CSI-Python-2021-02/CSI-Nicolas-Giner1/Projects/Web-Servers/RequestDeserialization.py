from asyncore import loop

# This will be necessary to create the directory for the request files
import os

import json, ssl
from pathlib import Path

# Necessary for HTTP requests to read and copy the request data from the random data site
from urllib import response
import urllib.request

# This file will be needed to be deserialized and processed into the responses folder
from Nation import Nation

# Adding this code to avoid certificate validation or prevent any error
ssl._create_default_https_context = ssl._create_unverified_context

# Including the URL where I'll request the data from; in this case, it'll be random_nation
nationURL = "https://random-data-api.com/api/nation/random_nation?size=100"

# Creating a list to fill with the nation data
nations:Nation = []

# Putting this code here to create and open a 'responses' folder to put each request file
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.mkdir(myFolderPath)

# Executing a HTTP Request to read the website and copy the request information to the responses folder
for i in range(100):
    req = urllib.request.Request(nationURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

# Putting this code to loop the JSON items on the request and deserialize them into python objects 
    for r in requestData:
# This deserializes the data
        newNation:Nation = Nation(**r)
# This adds the object to a list
        nations.append(newNation)
# And this prints the address id
        print(newNation.uid)

# This here puts the request files to the the responses folder 
        myFilePath = os.path.join(myFolderPath, f'response{newNation.uid}.json')

        with open(myFilePath, 'w') as outfile:
            json.dump(newNation.__dict__, outfile)


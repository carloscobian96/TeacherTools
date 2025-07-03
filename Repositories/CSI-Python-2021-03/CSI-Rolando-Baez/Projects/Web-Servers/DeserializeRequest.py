import json, ssl
import urllib.request
import os
from pathlib import Path
from RandomBlood import RandomBlood

ssl._create_default_https_context = ssl._create_unverified_context

bloodURL = "https://random-data-api.com/api/blood/random_blood?size=100"

# Create directory
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')

addresses:RandomBlood = [] 

for x in range(100):

    req = urllib.request.Request(bloodURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    for r in requestData:  
        blood:RandomBlood = RandomBlood(**r)
        addresses.append(blood) 
        print(blood.id)

        myFilePath = os.path.join(myFolderPath, f'{blood.uid}.json')

        with open(myFilePath, 'w') as outfile:
            json.dump(blood.__dict__, outfile)
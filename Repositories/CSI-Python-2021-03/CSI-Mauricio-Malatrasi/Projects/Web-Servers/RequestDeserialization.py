import json, ssl
from pathlib import Path
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin
import os

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cryptocoinURL = "https://random-data-api.com/api/crypto_coin/random_crypto_coin?size=100"

# Create a list to populate with our data
cryptocoins:RandomCryptoCoin = [] 

# Execute HTTP Request
# req = urllib.request.Request(cryptocoinURL)
# requestData = json.loads(urllib.request.urlopen(req).read())

# Loop over JSON items and Deserialize them into python objects
# for r in requestData:  
#     # Deserialize 
#     cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)
#     # Add object to list
#     cryptocoins.append(cryptocoin) 
#     # Print id
#     print(cryptocoin.coin_name)

myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')

os.mkdir(myFolderPath)

for x in range(0,100):
    req = urllib.request.Request(cryptocoinURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    for r in requestData:  
        # Deserialize 
        cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)
        # Add object to list
        cryptocoins.append(cryptocoin) 
        # Print id
        print(cryptocoin.coin_name)
        myFilePath = os.path.join(myFolderPath, f"{cryptocoin.uid}.json")

        with open(myFilePath, 'w') as outfile:
            json.dump(cryptocoin.__dict__, outfile)
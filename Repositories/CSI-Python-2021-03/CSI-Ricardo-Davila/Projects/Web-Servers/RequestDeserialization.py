import json, ssl
import urllib.request
import os
from pathlib import Path
from RandomCrypto import RandomCrypto

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
addressURL = "https://random-data-api.com/api/crypto/random_crypto?size=100"

# Create a list to populate with our data
cryptos:RandomCrypto = [] 



myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
data = os.mkdir(myFolderPath,)

for x in range (0,100):
    # Execute HTTP Request
    req = urllib.request.Request(addressURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        # Deserialize 
        crypto:RandomCrypto = RandomCrypto(**r)
        # Add object to list
        cryptos.append(crypto) 
        # Print id
        print(crypto.uid)

        myOutputFilePath = os.path.join(myFolderPath, f"{crypto.uid}.json")
        with open(myOutputFilePath, 'w') as outfile:
            # json.dump(MyDataSet[0].__dict__,outfile)
            json.dump(crypto.__dict__, outfile)


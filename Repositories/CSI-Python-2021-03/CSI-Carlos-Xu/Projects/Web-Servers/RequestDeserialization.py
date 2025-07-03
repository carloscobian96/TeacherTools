import json, ssl
from random import Random
import urllib.request
from RandomPhoneNumber import RandomPhoneNumber
import os
from pathlib import Path

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
phonenumberURL = "https://random-data-api.com/api/phone_number/random_phone_number?size=100"

# Create a list to populate with our data
phoneNumbers:RandomPhoneNumber = [] 




myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
data = os.mkdir(myFolderPath,)

# Loop over JSON items and Deserialize them into python objects



for x in range(0,100):
    # Execute HTTP Request
    req = urllib.request.Request(phonenumberURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    for r in requestData:
        # Deserialize 
        phoneNumber:RandomPhoneNumber = RandomPhoneNumber(**r)
        # Add object to list
        phoneNumbers.append(phoneNumber) 
        # Print phone number
        print(phoneNumber.phone_number)

        myOutputFilePath = os.path.join(myFolderPath,f"{phoneNumber.uid}.json")
        with open(myOutputFilePath, 'w') as outfile:
        # json.dump(MyDataSet[0].__dict__,outfile)
            json.dump(phoneNumber.__dict__,outfile)









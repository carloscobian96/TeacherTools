import json, ssl
import os
from pathlib import Path
import urllib.request
from Stripe import Stripe

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
stripeURL = "https://random-data-api.com/api/stripe/random_stripe?size=100"

stripe:Stripe = []

# Create a list to populate with our data
MyOutputPath = Path(__file__).parents[0]
MyOutputFilePath = os.path.join(MyOutputPath , 'responses')
os.mkdir(MyOutputFilePath)

# This is the loop makes 100 requests
for x in range(100):
    # Execute HTTP Request
    req = urllib.request.Request(stripeURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    # Loop over JSON items and Deserialize them into python objects
    for r in requestData: 
        # Deserialize  
        newStripe:Stripe = Stripe(**r)
        # Add object to list
        stripe.append(newStripe) 
        # Print id
        print(newStripe.id)

        MyOutputFile = os.path.join(MyOutputFilePath, f'{newStripe.uid}.json')

        with open(MyOutputFile, 'w') as outfile:
            json.dump(newStripe.__dict__ , outfile)


 
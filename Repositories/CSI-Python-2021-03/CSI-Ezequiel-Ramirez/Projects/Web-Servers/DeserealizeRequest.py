import json, ssl
from pathlib import Path
import urllib.request
from RandomBeer import RandomBeer
import os

ssl._create_default_https_context = ssl._create_unverified_context

BeerURL = "https://random-data-api.com/api/beer/random_beer?size=100"

beers:RandomBeer = []

# create directory
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'responses')

if not os.path.exists(myFilePath):
    os.mkdir(myFilePath)
    print("Directory " , "responses" , " created.")
else:
    print("Directory ", "responses" , " created.")

# loop 100 times
i = 1

Req = urllib.request.Request(BeerURL)
RequestData = json.loads(urllib.request.urlopen(Req).read())

while i <= 100:
    i += 1
    Req = urllib.request.Request(BeerURL)
    RequestData = json.loads(urllib.request.urlopen(Req).read())

    for r in RequestData:
        beer:RandomBeer = RandomBeer(**r)
        beers.append(beer)
        print(beer.name)

        myFinalPath = os.path.join(myFilePath, f"{beer.uid}.json")

        with open(myFinalPath, "w") as outfile:
            json.dump(beer.__dict__, outfile)
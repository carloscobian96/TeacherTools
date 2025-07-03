from ast import Delete
import json, ssl
import os
from pathlib import Path
import urllib.request
from InternetStuff import InternetStuff

#The only purpose this line serves is to prevent certificate validation
ssl._create_default_https_context = ssl._create_unverified_context

#Here I define "internetstuffURL" by defining it as the original URL I used
internetstuffURL = "https://random-data-api.com/api/internet_stuff/random_internet_stuff?size=100"

#Here I define both "myPath" and "myFolderPath". I also create a directory. 
myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.makedirs(myFolderPath)

#Here I create a list to populate with the data that I will create.
internetstuffs:InternetStuff = []

#I execute HTTP Request and I loop over Json items and Deserialize them into python objects
for i in range(100):
    req = urllib.request.Request(internetstuffURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    for r in requestData:
        current_internetstuff =InternetStuff(**r)
        internetstuffs.append(current_internetstuff)
        print(current_internetstuff.id)
        myFilePath = os.path.join(myFolderPath, f"{current_internetstuff.uid}.json")

        with open(myFilePath, 'w') as outfile:
            json.dump(current_internetstuff.__dict__, outfile)

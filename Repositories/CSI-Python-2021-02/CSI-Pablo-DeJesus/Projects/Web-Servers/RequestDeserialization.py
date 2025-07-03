import json, ssl
import os
from pathlib import Path
import urllib.request
from Food import Food

ssl._create_default_https_context = ssl._create_unverified_context

FoodURL = "https://random-data-api.com/api/food/random_food?size=100"

food:Food = [] 

myPath = Path(__file__).parents[0]
myFolderPath = os.path.join(myPath, 'responses')
os.makedirs(myFolderPath)

for x in range(100):
    
    req = urllib.request.Request(FoodURL)
    requestData = json.loads(urllib.request.urlopen(req).read())


    for r in requestData:
        current_food= Food(**r)

        food.append(current_food) 
        print(current_food.uid)

        myFilePath = os.path.join(myFolderPath, f"{current_food.uid}.json")
        with open(myFilePath, 'w') as outfile:
            json.dump(current_food.__dict__, outfile)
                
                #Process: # This is discouraged but it will avoid certificate validation (prevents error)
                #Make folder for requests named responses
                # This is the URL from which we will request the data
                # Create a list to populate with our data
                # Loop over JSON items and Deserialize them into python objects
                
                #make the request
                #derealize
                #add object to list
                #print id
            #create certain files       
        
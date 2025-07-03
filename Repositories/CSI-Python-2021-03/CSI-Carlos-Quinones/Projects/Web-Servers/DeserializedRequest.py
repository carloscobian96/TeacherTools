import json, ssl
import urllib.request
from RandomHipsterStuff import RandomHipsterStuff
import os

ssl._create_default_https_context = ssl._create_unverified_context

hipUrl = "https://random-data-api.com/api/hipster/random_hipster_stuff?size=100"

hipWords:RandomHipsterStuff = []


directory  = "Responses"
parent_dir  = r"C:\Users\carlo\Documents\CSI-Python-2021\Projects\Web-Servers"

mode = 0o666

path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
save_path = r"C:\Users\carlo\Documents\CSI-Python-2021\Projects\Web-Servers\Responses"

for x in range(0,10001):
    req = urllib.request.Request(hipUrl)
    requestData = json.loads(urllib.request.urlopen(req).read())
    for r in requestData:  
        
        # Deserialize 
        hipsterWord:RandomHipsterStuff = RandomHipsterStuff(**r)
        # Add object to list
        hipWords.append(hipsterWord)
        file_name = f"{x}.json"
        
        completeName = os.path.join(save_path, file_name)
       
        with open(completeName, "w") as outfile:
            json.dump(hipsterWord.__dict__,outfile)

        print(hipsterWord)
        # Print id
       # print(hipsterWord.words)


import json
import os
from pathlib import Path
from RandomCrypto import RandomCrypto

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_crypto.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
crypto:RandomCrypto = RandomCrypto(**data)

# Print data from the object
print(f"id: {crypto.id}")
print(f"uid: {crypto.uid}")
print(f"md5: {crypto.md5}")
print(f"sha1: {crypto.sha1}")
print(f"sha256: {crypto.sha256}")
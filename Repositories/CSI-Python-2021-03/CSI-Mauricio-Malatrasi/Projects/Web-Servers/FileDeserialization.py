import json
import os
from pathlib import Path
from RandomCryptoCoin import RandomCryptoCoin

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_crypto_coin.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**data)

# Print data from the object
print(f"ID: {cryptocoin.id}")
print(f"UID: {cryptocoin.uid}")
print(f"Coin Name: {cryptocoin.coin_name}")
print(f"Acronym: {cryptocoin.acronym}")
print(f"Logo: {cryptocoin.logo}")
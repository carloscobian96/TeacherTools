import json
import os
from pathlib import Path
from Stripe import Stripe

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_stripe.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
stripe:Stripe = Stripe(**data)

# Print data from the object
print(f"ID: {stripe.id}")
print(f"UID: {stripe.uid}")
print(f"valid_card: {stripe.valid_card}")
print(f"token: {stripe.token}")
print(f"invalid_card: {stripe.invalid_card}")
print(f"month: {stripe.month}")
print(f"year: {stripe.year}")
print(f"ccv: {stripe.ccv}")
print(f"ccv_amex: {stripe.ccv_amex}")
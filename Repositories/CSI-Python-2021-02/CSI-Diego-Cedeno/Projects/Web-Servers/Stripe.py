import json 

class Stripe:
    def __init__(self, id:int, uid:str, valid_card:str,
     token:str, invalid_card:str, month:str, year:str,
      ccv:str, ccv_amex:str):

      self.id = id
      self.uid = uid
      self.valid_card = valid_card
      self.token = token
      self.invalid_card = invalid_card
      self.month = month
      self.year = year
      self.ccv = ccv
      self.ccv_amex = ccv_amex

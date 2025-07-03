import random
import json, ssl
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

#Hangman pictures 
HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       ☹   |
           |
           |
          ===''', '''
       +---+
       ☹   |
       |   |
           |
          ===''', '''
       +---+
       ☹   |
      /|   |
           |
          ===''', '''
       +---+
       ☹   |
      /|\  |
           |
          ===''', '''
       +---+
       ☹   |
      /|\  |
      /    |
          ===''', '''
       +---+
       ☹   |
      /|\  |
      / \  |
          ===''']


# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cryptocoinURL = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"
req = urllib.request.Request(cryptocoinURL)
r = json.loads(urllib.request.urlopen(req).read())

cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)

# print(cryptocoin.coin_name)       This is used for any bugs that could happen in Hangman.

AttemptedLetters = []      #The bank for the attempted letters 

specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", "="]   #Special characters that can't be used in the game

def getInput(): #defining getInput
   while(True):
      guess=input("What is your guess?").lower()   
      if guess.isnumeric()== True :
         print("Must be a letter.")
         continue

      if len(guess) !=1 :
         print("Must be only one letter!")
         continue

      # for i in specialChar:
      if not guess.isalpha():
         print("Can't include special characters.")
         continue

      if (guess in AttemptedLetters):  #Used to identify the letters you've already used so you cant use them again.
         print("You already used this letter.")
         continue
      

      AttemptedLetters.append(guess)
      return guess


def printword():  #Defining print word
   temp:str= ""
   len(cryptocoin.coin_name.lower())
   for letter in cryptocoin.coin_name.lower() :
      # print(letter)
      
      if letter in AttemptedLetters:   #Creating a temporary variable
         temp+= letter
      else: 
         temp+= "_ "
   print(temp)
   return temp

  # if letter not in my word, increment counter
def printStep():
   global counter    #Here, we're implementing the counter
   counter = 0
   for letter in AttemptedLetters:
      if letter not in cryptocoin.coin_name.lower():
         counter = counter + 1
   print(HANGMAN_PICS[counter])
   print(str(AttemptedLetters).replace('\'','').replace('[','').replace(']',''))
   # print(f"Used Letters: {AttemptedLetters}")


while True:                      #Making a loop so if you lost, it'll start you over again with a new word.
   print("Starting Game")
   AttemptedLetters = []
   r = json.loads(urllib.request.urlopen(req).read())
   cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)
   while True :
      
      printStep()
      temp = printword()
      getInput()
      
      
      # break condition 
      if(temp == printword):
         print("YOU'VE WON!")             #If you guess the word correctly, the game tells you you've won
         print("---------------------")   #The division of the word you guessed correctly and a new word
         break

      if(counter == 6):                #Making it so if you guess 6 times incorrectly, it'll end the game and print you've lost.
         print("YOU'VE LOST")          #After this breaks, it'll start over again with a new word and it'll start the hangman all over.
         print(f"The word was: {cryptocoin.coin_name}")
         print("---------------------")
         break
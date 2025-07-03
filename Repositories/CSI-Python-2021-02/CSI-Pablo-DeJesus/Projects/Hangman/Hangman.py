from ast import Break, If
from ctypes.wintypes import WORD
from lib2to3.pytree import LeafPattern 
import ssl 
import urllib
import urllib.request
import json
import random
import string
from RandomFood import RandomFood
#import everything necesarry for the code to run such as json, random, urllib ect

# ---===*===---
#   Variables
# ---===*===---

#create list with characters not allowed in-game  
Incorrect_integers = ["0","1","2","3","4","5","6","7","8","9"]
Incorrect_characters = ["`","~","!","@","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}","\\","|",";",":",",","<",".",">","/","?"]


# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

#create steps based on characters(be original)
steps = ["""
        |----------------+
        |                |
        |
        |
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |                |
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|
        |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                |
        |
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                |
        |               /
        |
        |
        |
        |
        ___________________
        """,
        """
        |----------------+
        |                |
        |                O
        |               /|\\
        |                |
        |               / \\
        |
        |
        |
        |
        ___________________
        """]

# ---===*===---
#   Functions
# ---===*===---


# # len(food.ingredient)
# def tempFormat(temp):
#   #define variable
#   tempFormat=""
#   #for loop 
#   for i in range(len(temp)):
#     #append letter
#     tempFormat = tempFormat + f"{temp[i]} "
#   #return format
#   return tempFormat

def getWord():

    foodsURL = "https://random-data-api.com/api/food/random_food"
    #url which is used to access the random foods

    req = urllib.request.Request(foodsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    #requesting data site which has all the variables available for the game
    current_food:RandomFood = RandomFood(**requestData)
    #make array from words in name

    #return first word of the name
    return current_food.dish.upper()



    # x=1 #used to keep track of wrong guesses



# print (RandomFood)
#print food ingredient 

def get_input():
   
    while(True): 
        letter = input("Name Letter: ").upper()

        # Input validation
        if(len(letter) != 1):
            print("error 101:only letters are allowed") #print message if charater is not allowed
            continue

            
        if( letter in Incorrect_characters or letter in Incorrect_integers):
            print("error 101:incorrect letter or character")
            continue

        
        return letter
        # the past lines used length to find if player used only one letter and used if else logic to make sure the player does not repear used letters or incorrect/unavaileble letters)
           
 
 

def printWord(myWord,attemptedletters):
    # letter = list(string.ascii_lowercase())
    #grab all the lowercase letter in ascii instead of putting them all in a list(- credits to Hermann Bauer and prof Carlos Cobian for this line)
    # attemptedletters = []
        #array of attempted letters
    temp:str = ""
    counter = 0
    for letter in myWord:
        if (letter not in attemptedletters):
            temp = temp + "_ "
                # return wrong_letter #the past three lines used if else logic to grab the results of letters entered
        else:
            temp = temp + letter + " "
            counter = counter + 1
        # if (letter in myWord): 
        #     temp = temp + letter #results for letters entered using tem[]
            
        # else:
        #     temp = temp + "_" #if the letter is wrong
            
    print(temp)
    return counter

        
def get_step(myWord, attemptedletters): 
 #grabing variables from other functions to use in this one
    step = 0
    for letter in attemptedletters: #I tried to grab the function in which this en the variable in the net lime come from but  it would still report a problem
        if(letter not in myWord):
            step = step + 1

    return step
       
    




# ---===*===---
#   Game Logic
# ---===*===---
def play():
   
    while True:
        print("Starting new Game")
        myWord = getWord()
        attemptedletters = []
        
        while True:
            #the last lines I created a function and god word and grabbed steps to restart game 
            myStep = get_step(myWord, attemptedletters)
            print( steps[ myStep ] )

            counter = printWord(myWord,attemptedletters)
            letter = get_input().upper() 
            attemptedletters.append(letter)
            
            if( len(myWord) == counter):
                print("game won")
                break
            
            if(myStep == 7):
                print("game lost")
                break
            
            
play()
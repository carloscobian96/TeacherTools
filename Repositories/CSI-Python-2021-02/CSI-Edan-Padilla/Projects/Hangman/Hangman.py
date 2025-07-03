
from cgitb import reset
import json, ssl

import random
import urllib. request
from randomname import Name 

def getWord():


    ssl._create_default_https_context = ssl._create_unverified_context
    
    nameURL = "https://random-data-api.com/api/name/random_name"
   
    request = urllib.request.Request(nameURL)
    
    requestURL = json.loads(urllib.request.urlopen(request).read())

    current_name = Name(**requestURL)

    return current_name.name.upper()

   


steps = ["""
        __________________
        |                 |
        |                 |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |                 🎽
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |                 🎽🤳
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |                 🍆
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |                 🍆
        |                   🦿
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |                 🍆
        |                🦵🏽 🦿
        |
        |
        |
        |
        |
        |
        """]
        #This is the drawing of the hangman and each steps are printing.

# print(steps[0])

wrong_numbers = ["0","1","2","3","4","5","6","7","8","9"]
wrong_symbols = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","\\","|",":",";","'","<",">",",",".","?","/"] 
# This is telling what are the wrong symbols and numbers that you can't put in the hangman.

def getInput():
    while(True):
        letter =  input( "Try to find the word to win the game of Hangman by finding the letters: " )
        #This are the instruction to play hangman

        if (len(letter) !=1):
            continue 

        if letter in wrong_symbols:
            print("Wrong, you are bad 👎🏽")
            continue 
            #This code is telling you the is you put a wrong symbols print the sentence.
        if letter in wrong_symbols:
            print("Again, why are you bad?😐")
            continue 
            #This code is telling you the is you put a wrong symbols print the sentence.

        if letter in attemptedletters:
            print("Bad 💩")
            continue 
            # This code is telling you if you use a letter that you already use print the sentence.

        attemptedletters.append(letter.upper())
        return letter.upper()
        

def printword():
    temp:str=""
    for letter in myWord:
        if letter in attemptedletters:
             temp += letter
        else:
            temp +="_"
            
    return temp

def printsteps():
    phases = 0
    for letter in attemptedletters:
        if letter not in myWord:
            phases = phases +1
    print(steps[phases])
    return phases
    
    
#While true to keep game restarting
while True:
    #reset variables
    myWord = getWord()
    print(myWord)
    attemptedletters = []
    #WHile True per game
    while True:
        #assign variable to keep track of steps and temp
        phases = printsteps()
        temp = printword()
        print(temp)

        #check if word is guessed

        if myWord == temp:
            print("Game won")
            break
        #Get input

        getInput()

        #If word is wrong and step more than 7 lose

        if phases >= 7:
            print("Game lost")
            break
  
    # while True:
    #     myWord = getWord()
    #     used = []
  
    




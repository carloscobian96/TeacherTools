
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

# print(steps[0])

wrong_numbers = ["0","1","2","3","4","5","6","7","8","9"]
wrong_symbols = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","\\","|",":",";","'","<",">",",",".","?","/"] 


def getInput():
    while(True):
        letter =  input( "Try to find the word to win the game of Hangman by finding the letters: " )

        if (len(letter) !=1):
            continue 

        if letter in wrong_symbols:
            print("Wrong, you are bad 👎🏽")
            continue 

        if letter in wrong_symbols:
            print("Again, why are you bad?😐")
            continue 

        if letter in attemptedletters:
            print("Bad 💩")
            continue 

        attemptedletters.append(letter.upper())
        return letter.upper()


def printword():
    temp:str=""
    for letter in myWord:
        if letter in attemptedletters:
             temp += letter
        else:
            temp +="_"
            #phases = phases + 1
    return temp

def printsteps():
    phases = 0
    for letter in attemptedletters:
        if letter not in myWord:
            phases = phases +1
    print(steps[phases])
    return phases
    
    

while True:
    myWord = getWord()
    print(myWord)
    attemptedletters = []
    
    while True:
        phases = printsteps()
        temp = printword()
        print(temp)

        if myWord == temp:
            print("Game won")
            break

        getInput()

        if phases >= 7:
            print("Game lost")
            break
  
    # while True:
    #     myWord = getWord()
    #     used = []
  
    




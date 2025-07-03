# Hangman Rubric: CSI-Pablo-DeJesus

## Score: 87/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 28 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 15 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 0 | 
| game progression          | 10 | 9 | 
| restart game              | 5  | 5 | 

<br>

### Submitted Work: 

```python


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
```




# Instructions:

<div style="text-align:center">
        <img    src="https://media.istockphoto.com/illustrations/simple-illustration-of-hangman-game-illustration-id1196954772?k=20&m=1196954772&s=612x612&w=0&h=nzsr9bCwxp9xW3dp-nBJeXE7TVGqnWtdJpbaXvEyl3E="
                width="50%" 
                height="50%" />          
</div>

<br>

# Hangman `100pts Total`

<br>

### Instructions: `(30pts)`
* Create `Hangman.py` in this folder.
* Define a function for each objective.
* Document every line of the code.


<br>

## Select a random word. `(5pts)`
You may select a random word by one of 2 ways:
1. Create a list with at least 20 words and use `random()`
2. Fetch a random Word from an API. This may be done by using the *HTTP Request deserialization* code used in `Web-Servers`.

Print out it's length represented by underscores:

eg. MAGISTERIO
``` 
_ _ _ _ _ _ _ _ _ _
```

<br>

## Create a multiline string array for each step of the game. `(5pts)`
```python
steps = [
        """
        1
        """,
        """
        2
        """]
```

<br>

## Validate input `(10pts)`
Accept a single character from the user as input. You must ensure to receive a valid character.
* A single character long
* Not a number
* Not a symbol
* User has not attempted the letter already.
  * Create a list to store attempted characters
* Must handle lower case and upper case letters.

<br>

## Find matches in your word. `(10pts)`
Print out underscores combined with successfully matched characters.
``` 
M _ G _ S _ E _ I _
```

<br>

## Display the current step of the game by addressing it's index of the array. `(10pts)`
You must develop a mechanism to keep track of which step you're on base of failed attempts.
```python
# Example of printing the fist step in hangman.
print(steps[0])
```

<br>

## To-Do:
1. Display attempted letters List. `(10pts)`
2. Logic for game progression.`(10pts)`
3. Loop to restart game. `(5pts)`
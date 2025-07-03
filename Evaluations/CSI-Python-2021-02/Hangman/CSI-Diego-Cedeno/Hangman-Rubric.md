# Hangman Rubric: CSI-Diego-Cedeno

## Score: 87/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 30 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 15 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 0 | 
| game progression          | 10 | 8 | 
| restart game              | 5  | 4 | 

<br>

### Submitted Work: 

```python


import json, ssl
from tkinter import Y
import urllib.request
from Dessert import Dessert

# This is used to prevent errors
ssl._create_default_https_context = ssl._create_unverified_context

def getWord():
    
    # This URL is used to request a word from the class Dessert
    DessertURL = "https://random-data-api.com/api/dessert/random_dessert"
    
    # Here creates a variable to ask for data
    req = urllib.request.Request(DessertURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    
    # Deserialize into a class
    newDessert:Dessert = Dessert(**requestData)
    return newDessert.variety.upper()

# This is the variable created for all the incorrect characters
attemptedCharacter = []

# On this part are the each steps that creates the hangman
Steps = ["""
|---------|
|         |
|         
|
|
|
|
|
""",
"""
|---------|
|         |
|        😂
|         
|
|
|
|
""",
"""
|--------|
|        |
|       😂
|        |
|       
|
|
|
""",
"""
|--------|
|        |
|       😂
|      --|
|        
|        
|
|
""",
"""
|--------|
|        |
|       😂
|      --|--
|        |
|       
|
|
""",
"""
|--------|
|        |
|       😂
|      --|--
|        |
|       / 
|
|
""",
"""
|--------|
|        |
|       😂
|      --|--
|        |
|       / \\
|
|
"""
]

# # This print starts the game
#print(Steps[0])

# # In this part it prints the word that it got from the data and puts each character an _
# print(len(newDessert.variety)*" _ ")

# The function its used so that the game tells you the characters that are errors in the game
def getInput():
    while(True):
        
        # ask for input and upper means that all the letters that are used are put on capital letter
        Character = input(f"name a letter for this dessert: ").upper()
        special_char = "[@_!#$%^&*()<>?/\|}{~:]"

        # Validate input
        if(len(Character) != 1):
            print("error, just type a letter: ")
            continue
        # Here the game recognizes that you used a number and tells you to use a letter
        if(Character.isnumeric()):
            print("error, no numbers, just type a letter: ")
            continue
        # The game recognizes that you used a sepcial character and tells you to use a letter
        if(Character in special_char):
            print("Error, no special character, just type a letter: ")
            continue
        # Here the game checks which letters have you typed and tells you that you already used them
        if(Character in attemptedCharacter):
            print("Error, you already used this letter ")
            continue
    
        # This is for used character that were typed
        attemptedCharacter.append(Character)
        return Character

# This function is used so that it stores every correct Character that you type
def printWord():
    Temp:str = " "
    for Character in newDessert:
        # the logic here is that if the letter that you typed here is not correct the lines stay the same
        if Character not in attemptedCharacter:
            Temp +="_"
        # Here if the letter that you typed is correct the line is replaced with the letter that goes in that line
        else:
            Temp += Character     
    print(Temp)
    

# This is used to store the errors you do when putting the Character, the function adds 1 to each one you get wrong
def stepsErrors():
    error = 0
    for Character in attemptedCharacter:
        # Here it adds the step to each letter you put that is not in the word
        if(Character not in newDessert):
            error = error + 1
    return error

# The following part is the while True which will keep the game going and the game restarts
while True: 
    newDessert = getWord()
    attemptedCharacter = []
    
    while True:
        error = stepsErrors()
        # Here after the game reaches the 7 steps the game gives the message to the user that the game is over and then starts the new game
        if(error == 7):
            print(f"Game Over, you are a loser, the word that you didn't guessed was {newDessert}")
            print("---------------------")
            print("New Game")
            break
        # Here it prints the steps againg for the new game
        print(Steps[error])
        printWord()
        getInput()

        


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
# Hangman Rubric: CSI-Andres-Rodriguez

## Score: 78/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 25 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 15 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 0 | 
| game progression          | 10 | 8 | 
| restart game              | 5  | 0 | 

<br>

### Submitted Work: 

```python


import json, ssl
from typing import Counter
import urllib.request
from Cannabis import Cannabis
import urllib.request

#characters used list
used=[]

def get_cannabis():
# This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
    cannabisURL = "https://random-data-api.com/api/cannabis/random_cannabis"

#Api request
    req = urllib.request.Request(cannabisURL)
    r = json.loads(urllib.request.urlopen(req).read())

    cannabis:Cannabis = Cannabis(**r)

    return cannabis.strain.upper()


# create var to store the value of get_cannabis()



# print(len(myCannabis) * "_ ")

#drawings of my hangman

hang = ["""
H A N G M A N - 

   <====>
   |   l
       l
       l
       l
       l
<=======>""", 
"""
H A N G M A N - 

  <====>
  I   l
  *   l
      l
      l
      l
<=======>""", 
"""
H A N G M A N -

  <====>
  I    l
  *    l
  I    l
       l
       l
<=======>""", 
"""
H A N G M A N - 

  <====>
  I    l
  *    l
 $I    l
       l
       l
=========""", 
"""
H A N G M A N - 

  <====>
  I    l
  *    l
 $I$   l
       l
       l
<=======>""", 
"""
H A N G M A N - 

  <====>
  I    l
  *    l
 $I$   l
 (     l
       l
<=======>""", 
"""
H A N G M A N - 

 <=====>
  I    l
  *    l
 $I$   l
 ( )   l
       l
<=======>""",
]

#incorrect letters in my hangman
UsedLetters = [] # the different letters that you already used during the game


def getInput():
    invalid_characters = ("1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","{","}","[","]",";","'","<",",",".",">","/","?","|") #charactres that you can't use
    
    while(True):
        guess=input("Your guess is").upper() 
        if guess .isnumeric()== True :
            print("Needs to be a letter")     #if you put a number it prints you "needs to be a letter"
            continue

        if len(guess) !=1 :
            print("Not more than one letter")    #if you put more than one letter it prints you "not more thatn one letter"
            continue 

        if not guess.isalpha() and guess != ' ':
            print("No special characters")  # if you use one character that is no a number or a letter it prints you "no special character"
            continue

        if (guess in UsedLetters):
            print("Letter is already used") # if you put the same letter twice you it prints you "letter is already used"
            continue

        UsedLetters.append(guess) 
        return guess

# print(getInput())

def printword():
    temp:str=""
    for letter in myCannabis :
    # letter in(UsedLetter)
        if letter not in UsedLetters :
            temp = temp + "_"
        else:
            temp = temp + letter
    return temp

def printStep():
    counter = 0 #putting the counter
    for letter in UsedLetters:
        if letter not in myCannabis:
         counter= counter + 1

    print(hang[counter])

while True :
    myCannabis = get_cannabis().upper()

    #print(myCannabis)
    print("starting game ")   #if you finished the game print "starting game"
    IncorrectLetters = []     #print the incorrect letters in the new game

    while True:
        printStep()
        temp = printword()
        print(temp)
        getInput()

        if(temp == myCannabis): #do a break if "temp" is equal to "myword"
            print("game won")    #Prints when you win
            print("~~~~~~~~~~~~~~~~~~~~")       #Divides the games
            break #exit out of a loop when an external condition is triggered

        if(Counter == 7):  # do a break if you put 7 incorrect letter
            print("gamelost")    #Prints when you lose
            print("~~~~~~~~~~~~~~~~~~~~")       #Divides the games
            break #exit out of a loop when an external condition is triggered
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
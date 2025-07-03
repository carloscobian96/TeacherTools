# Hangman Rubric: CSI-Andres-Juncos

## Score: 86/100 Points
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
| restart game              | 5  | 3 | 

<br>

### Submitted Work: 

```python


import json, ssl
import urllib.request
from Coffee import Coffee

def getword():
    ssl._create_default_https_context = ssl._create_unverified_context

    #Here im requesting a random word from the class and pulling it here
    CoffeeURL = "https://random-data-api.com/api/coffee/random_coffee"

    req = urllib.request.Request(CoffeeURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    coffee:Coffee = Coffee(**requestData)
    return coffee.blend_name.upper()


#Here im creating each step for the game
steps = ["""
    |---------|
    |         |
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
    |         |
    |         O
    |
    |
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |         I
    |         I
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |         I--
    |         I
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |       --l--
    |         l
    |
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |       --l--
    |         l
    |        /
    |
    |
    """,
    """
    |---------|
    |         |
    |         |
    |         O
    |       --l--
    |         l
    |        / \\
    |
    |
    """,
    """

    """]

#Prints the first step, which is the start.
# print(steps[0])

#This prints the random word selected but the letters are replaced with _.
#print(len(coffee.blend_name)*"_")

#print(coffee.blend_name)


#This function is filtering every other input that isn't a letter, making surethere are no numbers, symbols or that only 1 letter is selected, and will return an error until 1 letter is put in.
def input_function():
    while(True):
        letter = input("Input letter:").upper()
        specialcharacter = "!@#$%^&*()+?_=,<>/"
        
        if(len(letter) != 1):
            print("Only type 1 letter")
            continue
        if (letter.isnumeric()):
            print("There are no numbers")
            continue
        if (letter in specialcharacter):
            print("Not a letter")
            continue
        if (letter in attemptedLetters):
            print("Letter already used")
            continue
        

        # append to list of used letters
        attemptedLetters.append(letter)
        return letter

#This is the logic used for every correct letter, which verifies the inputed letter, and if it is right, it replaces the _s for the correct letter inputed. If it is wrong, then it will leave it as it is.
def printword(myCoffee):

    Temp:str = ""
    for letter in myCoffee:
        if letter in attemptedLetters:
            Temp+= letter 
        else:
            Temp+= "_"
    print(Temp)
   

#This is the logic for every wrong letter. First it creates the variable "errors" to store the count for every wrong worc. Then, it verifies if the letter is wrong, and if it is, it will raise the errors count by 1 and print the next step.
#This will repeat until all 7 steps are passed, which will then say "GAME OVER" and reveal what the word was.
def getErrors(myCoffee):
    errors=0
    for letter in attemptedLetters:
        if letter not in myCoffee:
            errors=errors+1
            if errors==7:
                print("You lost 🗿🗿🗿🗿, the word was:")
                print(myCoffee)
            
    return errors
       

        

#This is what keeps the game going and will repeat all loops until the game is over.
while(True):
    attemptedLetters=[""]
    myword=getword()
    while(True):
        printword(myword)
        errors = getErrors(myword)
        print(steps[errors])
        # printsteps(myword,errors)
        input_function()
        
        if errors == 7:
            break

    



 



    

    


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
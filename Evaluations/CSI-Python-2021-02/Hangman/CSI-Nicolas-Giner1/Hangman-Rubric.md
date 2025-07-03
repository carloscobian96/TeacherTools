# Hangman Rubric: CSI-Nicolas-Giner1

## Score: 98/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 28 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 15 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 10 | 
| game progression          | 10 | 10 | 
| restart game              | 5  | 5 | 

<br>

### Submitted Work: 

```python


from ast import While
import json, ssl
from pipes import Template
from tempfile import template
from tracemalloc import start
# Import urllib.request so that we're able to import the link to the random-data api page, from which we gather the random_nation nationalities.
import urllib.request
# Import Nation files so that the random_nation nationalities are used for the hangman game.
from Nation import Nation

def get_word(): 
    ssl._create_default_https_context = ssl._create_unverified_context

    nationURL = "https://random-data-api.com/api/nation/random_nation"

    req = urllib.request.Request(nationURL)

    requestData = json.loads(urllib.request.urlopen(req).read())

    newNation:Nation = Nation(**requestData)

    return newNation.nationality.upper()


# This array will be used so that the game is able to progress after each mistake you make.
# It begins at 0 and once it passes 6, it will declare a "game over".
Steps = ["""
|------------|
|
|
|
|
|
|
""",
""""
|-----------|
|           o
|          
|          
|
|
|
""",
"""
|-----------|
|           o
|           |
|          
|
|
|
""",
"""
|-----------|
|           o
|          /|
|          
|
|
|
""","""
|-----------|
|           o
|          /|\\
|          
|
|
|
""",
"""
|-----------|
|           o
|          /|\\
|          /
|          
|
|
|
""",
"""
|-----------|
|           o
|          /|\\
|          / \\
|          
|
|
|
"""
]



        # This will make it so that the hangman's words/names will be covered by underscores.
        # Further on, these will be programmed to be replaced by the correct letters you guess.

        # This will register whether your inputs are invalid numbers and symbols or already used letters and inputs that go beyond the one-character limit.
def get_input():
    # The while(True) code is there to maintain a loop that will pause and continue for whatever input you make in this game.
    while(True):
        special_character = "[@_!#$%^&*()<>?/\|}{~:]')"

        # # This will make it so that the hangman's words/names will be covered by underscores.
        # # Further on, these will be programmed to be replaced by the correct letters you guess.
        # print(len(newNation)*" _ ")

        # Obviously, this input prompts the game by asking the player to insert a letter for a nationality. 
        Start= input(f"Welcome to Hangman! Name a letter for this nationality: ").upper()

        # This registers when you've gone past the character limit.
        if(len(Start) != 1):
            print("Error. It's too long. Try again")

            # There's a 'continue' code so that the game continues its loops and prompts you to insert another letter.
            continue

        # This registers when you enter a number.
        if(Start.isnumeric()):
            print("Error. Don't use a number. Try again.")
            continue 

        # This registers when you enter a special character.
        # In this case, however, you have to make a variable that covers each and every special character in your keyboard so that the game can register it properly.
        if(Start in special_character):
            print("Error. Don't use special characters.")
            continue 

        # The same can be said about this, with the exception being that you have to make another variable for a different group.
        # The attempted_letters variable can be found as an empty list in the beginning of the code since it varies per usage and specific nationality.
        if(Start in attempted_letters):
            print("Error. Letter has already been used. Try again.")
            continue 
        attempted_letters.append(Start)

        #The 'return Start' ('Start' being the input that starts the game) makes the game loop back and prompt you once again to input another letter after correctly inputting a letter. 
        return Start

# Now, this function makes it so that the correct letters you input replace the empty blanks for the nationality you're trying to guess.
def print_word():

# The 'tempt' is a temporary line of code that will eventually be replaced by the correct letter you input. 
    Tempt:str=" "
    for Start in newNation:
        if Start in attempted_letters:
        # If you guess a correct letter in this nationality, the 'tempt' code will then be replaced by it.
            Tempt+= Start
        else:
        # If not, then it remains as the same empty blank it already was.
            Tempt+= " _ "
    print(Tempt)


    

# This function makes it so that the game registers each mistake you make and the game. 
# It also makes a logical progression system that follows the hangman's rules.

def countMistakes():
# Remember how each step in the hangman game is represented by the 'Steps' array in the beginning of the code?
# Each variable in that array is organized by a binary that registers them from 0 to 5.
# By turning the mistakes into a number variable, you artifically program the game into registering each step.
    mistake = 0
    for Start in attempted_letters:
        # For each mistake you make, the variable's value changes, thus affecting the progression of the game.
        if Start not in newNation:
            mistake = mistake + 1
            print (f"Attempted Letters: [{Start}]") 
    return mistake


def countCorrect():
    correct = 0
    for letter in newNation:
        if letter in attempted_letters:
            correct = correct + 1

    return correct

while (True):

    newNation = get_word()
    attempted_letters = [] 
    while True:
        mistake = countMistakes()
        print (Steps[mistake])
        print_word()
        get_input()

        # Lose Game
        if(mistake > 5):
            print (f"Game Over. Start again! The word was: [{newNation}]")
            print("-----------------------------------------------------------")
            break

        # Win Game
        if(countCorrect() == len(newNation)):
            print (f"Game Won. Start again!")
            print("-----------------------------------------------------------")
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
# Hangman Rubric: CSI-Carlos-Xu

## Score: 100/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 30 | 
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


import random # allows me to get random things, in this case, a list of words 

# this is a list of words (sports) that I will use in my game
word_list = ["gimnasia", "tenis", "ciclismo", "rugby", "boliche", "vela", "baloncesto", "voleibol", "remo", "surfing", "patinaje", "balompie", "natacion", "pelota", "ajedrez", "golf", "badminton", "boxeo", "esgrima", "hockey"]


# Different steps of my game when the user puts an incorrect character.

steps = [""" 

--------
|
|
|
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|
|
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|     |
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|    -|-
|
|
>>>>>>>>>>>>>>>>
""",
"""
--------
|     |
|     O
|    -|-
|    ? ?
|
>>>>>>>>>>>>>>>>


"""]
        

# This shows that the player can't use this special characters in order to guess the word.
invalid_specialcharacters= ["!","@","~","`","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",":",";","'","<",",",".",">","/","?"]

# This shows that the player can't pick numbers in order to guess the word.
invalid_numbers= ["9","8","7","6","5","4","3","2","1","0"]


# This variable means all the characters that the player might try. This characters can't be neither special characters or numbers.
attemptedcharacters=[]


# This function grabs a word randomly from the word list which the user will need to guess (sports list).
def implement_word():
    return random.choice(word_list)


# Defining the input function. This function check if the character entered by the player is in the word or not.
def get_input():

# This is the space where the player can try to guess a letter of the randomly given word by the game.
    while(True):
        letter = input("Choose your letter").lower()

# This tells the player that only one letter is allow to guess the word.
        if(len(letter)!= 1):
            print("Only choose one letter")
            continue

# This tells the player that he can't pick up a special character to guess the word.
        if(letter in invalid_specialcharacters):
            print("It can't be a special character")
            continue

# This tells the player that he can't pick up numbers to guess the word.
        if(letter in invalid_numbers):
            print("No numbers are allowed")
            continue
# This tells the player that he is trying to guess the word with a letter that he already used earlier in the game.
        if letter in attemptedcharacters:
            print("You have already used this letter")
            continue
        
        # This line keeps track of the characters used by the player.
        attemptedcharacters.append (letter)
        return letter


# Defining the function when printing the word.
def print_word():
    temp:str = ""
    # If the letter is not inside the characters attempted by the player, then it will be represented by an undersocre.
    for letter in my_word:
        if (letter not in attemptedcharacters):
            temp = temp + "_"
        # If the letter is inside the characters attempted by the player, then it will add the letter that was chosen by the player.
        else: 
            temp = temp + letter
    
    print(temp)

# This step shows that if the player's guesses are equal to the word of the hangman game (answer), then the program prints that the player has won.
    if temp == my_word:
        print("You win!")
        return True
    return False
    

# It is printing the steps of my hangman's puppet when the player chooses an incorrect letter.
def printStep():
    # Variable named counter
    counter = 0
    # If the letter chosen by the player is not in the word, then it will add one part of the puppet's body. 
    # This means that the player lost an attempt to guess the word and win the game.
    for letter in attemptedcharacters:
        if letter not in my_word:
            counter = counter + 1

    print(steps[counter])


# If the player misses five letters (five attempts) that are not in the word, then the player will lose the game because the hamgman's body will be completed. 
    if counter == 5:
        print("Game Over")
        print(f"You would won if you put {my_word}!!!")
        return False
    return True

# This while loop is responsable for beginning the game and calling the previously defined functions.   
while True:
    print("Starting game")
    my_word = implement_word()
    attemptedcharacters = []

    while True:
        if(not printStep()):
            break
    # The function of this string is to print all the letters that were used by the player to avoid repeting them again.
        MyWordString = str(attemptedcharacters).replace('\'','').replace('[','').replace(']','')
        print(f"Letters already used: {MyWordString} ")
        if(print_word()):
            break
        get_input()
# The program prints this after the game ends either the player won or not.
    print ("The game will start again right now.")
        


       
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
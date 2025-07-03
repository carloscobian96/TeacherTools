# Hangman Rubric: CSI-Rolando-Baez

## Score: /100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 |  | 
| random word               | 5  |  | 
| multiline string array    | 5  |  | 
| Validate input            | 15 |  | 
| Find matches              | 10 |  | 
| Display the current step  | 10 |  | 
| Display attempted letters | 10 |  | 
| game progression          | 10 |  | 
| restart game              | 5  |  | 

<br>

### Submitted Work: 

```python


import random

steps = ["""
 
      ___________
     [          []
     ]          []
                []
                []
                []
                []
                []
    ==============
""",
"""

      ___________
     [          []
     ]          []           
    / \         []
    \_/         []
                []
                []
                []
                []
    ==============

""",
"""
      ___________
     [          []
     ]          []           
    / \         []
    \_/         []
    | |         []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
    \_/ /       []
    | |/        []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
      \         []
       \        []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
    / \         []
   /   \        []
    ==============

"""
]
#This function chooses a random word from a list using random.choice and will then make that word the "Hangman Word" which is defined as hangmanWord
def get_word():
  possibleWords = ['ponce', 'guaynabo', 'fajardo', 'bayamon', 'carolina', 'cabo rojo', 'san juan', 'aguadilla', 'moca', 'lajas', 'arecibo', 'orocovis', 'cayey', 'corozal', 'salinas', 'arroyo', 'yabucoa', 'humacao', 'ceiba', 'luquillo']
  hangmanWord = random.choice(possibleWords)
  return hangmanWord

#This function is supposed to create a list titled "lettersList" in which letters will be put into once used for then to be used in other functions
def used_letters():
  lettersList = []
  maxTries = 15
  while len(lettersList) < maxTries:
    lettersList.append

#This function prints the blank spots of the word per letter
def print_word(hangmanWord):
  blank_word = len(hangmanWord) * '_'
  word = print(blank_word)
  return word

#This function will get the input and validate it using isalpha which will only use alphabetical characters
def get_input():
  while True:
    letter = input("Choose letter")
    if letter.isalpha():
      print("Choose a valid character (A letter from a to z)")
      continue
      
    return letter
 
 #This will check if the letter is found within the word or if it's not. If it's not the step will print giving the player one less chance to guess (if this worked correctly (it doesn't))
def word_check(letter, hangmanWord, lettersList):
      if letter not in hangmanWord:
        print('Incorrect guess...')
        lettersList.append(letter)
        print (steps[0])
        print(lettersList)
      if letter in hangmanWord:
        print('Correct Guess!')
        lettersList.append(letter)
        print(lettersList)

# After a letter is guessed, this function will check if that letter corresponds to a certain letter within the word and it will fill it in
def fill_blanks(letter, hangmanWord, lettersList):
  temp = ""
  for letter in hangmanWord:
    if(letter in lettersList):
      temp = temp + letter
    else:
      temp = temp + '_'

get_word()

print_word('hangmanWord')

get_input()

used_letters()

word_check()

fill_blanks()


    

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
# Hangman Rubric: CSI-Mauricio-Malatrasi

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


import random
import json, ssl
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

#Hangman pictures 
HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       ☹   |
           |
           |
          ===''', '''
       +---+
       ☹   |
       |   |
           |
          ===''', '''
       +---+
       ☹   |
      /|   |
           |
          ===''', '''
       +---+
       ☹   |
      /|\  |
           |
          ===''', '''
       +---+
       ☹   |
      /|\  |
      /    |
          ===''', '''
       +---+
       ☹   |
      /|\  |
      / \  |
          ===''']


# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cryptocoinURL = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"
req = urllib.request.Request(cryptocoinURL)
r = json.loads(urllib.request.urlopen(req).read())

cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)

# print(cryptocoin.coin_name)       This is used for any bugs that could happen in Hangman.

AttemptedLetters = []      #The bank for the attempted letters 

specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", "="]   #Special characters that can't be used in the game

def getInput(): #defining getInput
   while(True):
      guess=input("What is your guess?").lower()   
      if guess.isnumeric()== True :
         print("Must be a letter.")
         continue

      if len(guess) !=1 :
         print("Must be only one letter!")
         continue

      # for i in specialChar:
      if not guess.isalpha():
         print("Can't include special characters.")
         continue

      if (guess in AttemptedLetters):  #Used to identify the letters you've already used so you cant use them again.
         print("You already used this letter.")
         continue
      

      AttemptedLetters.append(guess)
      return guess


def printword():  #Defining print word
   temp:str= ""
   len(cryptocoin.coin_name.lower())
   for letter in cryptocoin.coin_name.lower() :
      # print(letter)
      
      if letter in AttemptedLetters:   #Creating a temporary variable
         temp+= letter
      else: 
         temp+= "_ "
   print(temp)
   return temp

  # if letter not in my word, increment counter
def printStep():
   global counter    #Here, we're implementing the counter
   counter = 0
   for letter in AttemptedLetters:
      if letter not in cryptocoin.coin_name.lower():
         counter = counter + 1
   print(HANGMAN_PICS[counter])
   print(str(AttemptedLetters).replace('\'','').replace('[','').replace(']',''))
   # print(f"Used Letters: {AttemptedLetters}")


while True:                      #Making a loop so if you lost, it'll start you over again with a new word.
   print("Starting Game")
   AttemptedLetters = []
   r = json.loads(urllib.request.urlopen(req).read())
   cryptocoin:RandomCryptoCoin = RandomCryptoCoin(**r)
   while True :
      
      printStep()
      temp = printword()
      getInput()
      
      
      # break condition 
      if(temp == printword):
         print("YOU'VE WON!")             #If you guess the word correctly, the game tells you you've won
         print("---------------------")   #The division of the word you guessed correctly and a new word
         break

      if(counter == 6):                #Making it so if you guess 6 times incorrectly, it'll end the game and print you've lost.
         print("YOU'VE LOST")          #After this breaks, it'll start over again with a new word and it'll start the hangman all over.
         print(f"The word was: {cryptocoin.coin_name}")
         print("---------------------")
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
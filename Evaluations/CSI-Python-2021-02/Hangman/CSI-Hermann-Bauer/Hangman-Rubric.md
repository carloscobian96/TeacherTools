# Hangman Rubric: CSI-Hermann-Bauer

## Score: 99/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 30 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 15 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 10 | 
| game progression          | 10 | 9 | 
| restart game              | 5  | 5 | 

<br>

### Submitted Work: 

```python


import urllib.request
from Beer import Beer
import json
import string
import ssl

#prevent error
ssl._create_default_https_context = ssl._create_unverified_context

#format word with spaces between letters
def tempFormat(temp):
  #declare variable
  tempFormat=""
  #for loop for letter in word
  for i in range(len(temp)):
    #append letter and space
    tempFormat = tempFormat + f"{temp[i]} "
  #return formatted
  return tempFormat
      
def getWord():
    # This is discouraged but it will avoid certificate validation (prevents error)
    # This is the URL from which we will request the data
    beerURL = "https://random-data-api.com/api/beer/random_beer"
 
    # Loop over JSON items and Deserialize them into python objects
    req = urllib.request.Request(beerURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    # Deserialize into class
    current_beer:Beer = Beer(**requestData)
    #make array from words in name
    name = current_beer.name.split()
    #return first word of the name
    return name[0]

def printWord(word):
  #X used to keep track of incorrect guessed// starts at one because 0 is the first step
  x=1
  #print starting step
  print(steps[0])
  #list of all letters in lowercase
  letters = list(string.ascii_lowercase)
  #an arr of all the letters in the word
  lettersInWord = list(word)
  #arr of letter guessed
  lettersGuessed = []
  #temp is the temporary variable of the word, corrects letters are there, while letters not guessed are an underscore
  temp:str= ("_" * len(word))
  #prints temp with a space between each underscore
  print(tempFormat(temp))
  #for letter in word:
  while True:
    #input guessed letter
    letter = input("Input Guess: ").lower()
    #check if input is not in letter
    if letter not in letters:
      #if not ask user to input letter
      print("Please input letter.")
    #check if letter has been guessed
    elif letter in lettersGuessed:
      #if has been guessed ask user to input new letter
      print("Already guessed that")

    #check if letter is in word
    elif letter in lettersInWord:
      #append to guessed letters
      lettersGuessed.append(letter)
      #print formatted temp for user to read
      print(tempFormat(temp))
      #affirm user letter is in word
      print("Letter in word")
      #remind user of guessed words
      
      #replace letter in each ocurrance
      for i in range(len(lettersInWord)):
        #check if letter is in that place
        if letter == lettersInWord[i]:
          #replace underscore with letter
          temp = temp[:i] + lettersInWord[i] + temp[i + 1:]
          
          #check if temp is equal to word
          if temp==word:
            #print final word formatted
            print(tempFormat(temp))
            #return game won
            return 'Game won!'

      print(tempFormat(temp))

    #If letter not in word nor in letters guessed
    else:
      #tell user letter is incorrect
      print("Letter not in word")
      #print next step in hangman
      print(steps[x])
      #add one to incorrect guesses
      x+=1
      #append guess to letters guessed
      lettersGuessed.append(letter)
      #print formatted temp
      print(tempFormat(temp))
      #remind user of letters guessed
      myVar = str(lettersGuessed).replace("[", " ").replace("]", " ")
      print(f"Letters guessed: {myVar}")
    #if incorrect guessed above 6, the game is lost
    if x>6:
      print(word)
      return 'Game Lost'
        
steps = ["""
  -----
|  |   
|      
|      
|      
|      
=========
""", """
  -----
|  |   
|  😢   
|      
|      
|      
=========
""", """
  -----
|  |   
|  😢   
|  |   
|      
|      
=========
""", """
  -----
|  |  
|  😢   
| /|   
|      
|      
=========
""", """
  -----
|  |   
|  😢   
| /|\  
|      
|      
=========
""", """
  -----
|  |   
|  😢   
| /|\  
| /    
|      
=========
""", """
  -----
|  |   
|  😢   
| /|\  
| / \  
|      
=========
"""]

#restart game
while True:
  print("New Game")
  #lowercase word
  word = getWord().lower()
  print(printWord(word))
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
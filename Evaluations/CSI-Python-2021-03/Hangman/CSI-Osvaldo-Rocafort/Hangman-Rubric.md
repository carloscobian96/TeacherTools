# Hangman Rubric: CSI-Osvaldo-Rocafort

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


from ast import Break
import ssl
from turtle import reset
import urllib,json
from Colors import Colors
import urllib.request

used=[]
def get_color():
    # This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

    # This is the URL from which we will request the data
    colorsURL = "https://random-data-api.com/api/color/random_color"

    req = urllib.request.Request(colorsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    color:Colors = Colors(**requestData)
    
    return (color.color_name)

# myColor = get_color()
# print(myColor)


#Steps to create a hangman.
steps = ["""
    .-------.
    |       |
    |       O
    |      
    |      
    |^^^^^^^^^^^^^   
         """,
        """
    .-------.
    |       |
    |       O
    |       |
    |      
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|
    |
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|-
    |
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|-
    |      /
    |^^^^^^^^^^^^^
        """,
        """
    .-------.
    |       |
    |       O
    |      -|-
    |      / \\
    |^^^^^^^^^^^^^
    """
     
]
# for step in steps:
#     print(steps)
# print(steps[0])

# Naming all the invalid characters in the keyboard for hangman.
def getInput():
    Invalid_Characters= ("1","2","3","4","5","6","7","8","9","0","10","!","@","#","$","%","^","^","&","*","(",")","-","_","=","+","[","]","{","}",":",";",",","<",".",">","/","?")
#Inputing a letter to choose.
    while(True):
        letter = input("Choose letter").upper()
# Putting the length of the letter
        if(len(letter)!=1):
            print("error")
            continue
# If you put a character that is from the invalid list it puts error.   
        if(letter in Invalid_Characters):
            print("error")
            continue
# Adding the letters to the list     
        used.append(letter)
# Returning a letter       
        return letter
    
# It's defining print word and using temp
def printword():
    temp:str=""
# If the letter that I choose is a letter from the word then it adds the letter to form the word and if I put a letter that is not from the word there will be a space.
    for letter in myColor:
        if letter in used:
            temp=temp + letter
        else:
            temp= temp + "_"
 #printing temp           
    print(temp)
    return temp
    
    
#printing steps for the counter of the words that are printing      
def printSteps():
    counter= 0
    for letter in used:
        if letter not in myColor:
            counter= counter + 1
#printing steps counter           
    print(steps[counter])
    
    return counter
    
# printing the steps, input and words for the hangman game.       
while True:
    myColor = get_color().upper()
    used = []
 #printing steps
    while True:
        counter=printSteps()
        getInput()
        temp = printword()
        
        usedString = str(used).replace('\'','').replace('[','').replace(']','')
        print(f"Used Letters: {usedString}")
          
        if(temp == myColor):
            print("GAME WON")
        #restarting game
            
        # printing game over when you lose
        if(counter>4 ):
            print ("GAME OVER")
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
# Hangman Rubric: CSI-Nicolas-Barreras

## Score: 95/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 30 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 10 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 10 | 
| game progression          | 10 | 10 | 
| restart game              | 5  | 5 | 

<br>

### Submitted Work: 

```python

from random import gammavariate
import ssl
import urllib, json
from RandomFood import RandomFood
import urllib.request

# used characters list


# Giving a function to this code
def get_food():
    ssl._create_default_https_context = ssl._create_unverified_context  # This is discouraged but it will avoid certificate validation (prevents error)
    foodsURL = "https://random-data-api.com/api/food/random_food"   # This is my URL from the Api provider

# Request from URL to choose word    
    req = urllib.request.Request(foodsURL)
    requestData = json.loads(urllib.request.urlopen(req).read())
    food:RandomFood = RandomFood(**requestData)

    return food.ingredient.upper()

# Steps for Hangman
Steps= ["""
        /---------|
        |         |
        |
        |
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |         |
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |        -|
        |
        |
    -------------------
""",
"""
        /---------|
        |         |
        |         O
        |        -|-
        |
        |
    ------------------- 
""",
"""
        /---------|
        |         |
        |         O
        |        -|-
        |        ( 
        |
    ------------------- 
""",
"""
        /---------|
        |         |
        |         O
        |        -|-
        |        ( )
        |
    ------------------- 
""",
"""
        /---------|
        |         |
        |         0
        |        -|-
        |        ( )
        |
    ------------------- 
""",
]

#Giving a function to this code
def getInput():
    invalid_characters=["""
    1""","""2""","""3""",   #list of invalid characters
    """4""","""5""","""6""",
    """7""","""8""","""9""",
    """10""",""",""","""'""",
    """/""","""?""","""<""",
    """:""",""";""",""">""",
    """.""","""[""","""]""",
    """{""","""}""","""|""",
    """=""","""+""","""_""",
    """-""",""")""","""0""",
    """(""","""*""","""&""",
    """^""","""%""","""$""",
    """#""","""@""","""!""",
    """`""","""~""",
    ]  
    while(True):   
        #prints in the game "Choose Letter=" for your guess
        letter = input("Choose letter=").upper()

        if(len(letter)!= 1):
            print("error")
            continue
        # for a guess in the list of invalid characters prints error
        if(letter in invalid_characters):
            print("error")
            continue
        # if you guesed the same word again it prints already guessed letter
        if letter in used:
            print("Already guessed letter")

        used.append(letter)

        return letter

#Giving a function to this code
def printWord():
    temp:str=""

    for letter in myFood:   # this checks in if the letter is in myFood
        if letter in used:  # this tells the computer that is the letter is in the list of used
            temp= temp + letter # temp is
        else: temp= temp + "_"
    print(temp)
    return temp

#Giving a function to this code
def printStep():
    counter= 0  # keeps track of the steps you are
    for letter in used: #this checks if the letter is in used 
        if letter not in myFood: #this tells the computer that the word is not in myFood that is the letter
            counter= counter + 1 #this add a step forevery error
    print(Steps[counter])   #this prints the steps
    return counter  #this sends this code to whiletrue/ print steps

while True:
    myFood = get_food() # this place the word in get food
    used = [] # this the used list
       
    while True:
        counter = printStep() # this is the return 
        getInput()
        temp = printWord()
        usedString = str(used).replace('\'','').replace('[','').replace(']','')# this is from planets.py this eliminates all the brackets,qoutes and replace it with nothing
        print(f"Used Letters: {usedString}")    #this prints Used Letter for keeping a list and indicate you for the word that you already used

#this tells us if we won or lost the game
        if(temp == myFood):   #
            print ("""                                                                   
                      _______          ___          ____     ____     ________       ____               ____    ________      _____   ___
                    /  GGGGGG|        /  A\        |  MM|   /  MM|   |  EEEEEE|     |  WW|             |  WW|  /  OOOOOO\    |  NNN\ | NN|
                   |  GG             /  AAA\       |  MMMM|/ MMMM|   |  E|---/       \  WW\   _____   /  WW/  /  OO-\  OO\   |  NNNN\| NN|
                   |  GG   __       /  A   A\      |  MM MMMMM MM|   |  EEEE|         \  WW\ /  WWW\ /  WW/   | OO|  |  OO|  |  NN|NN| NN|
                   |  GG  |GG|     /  AAAAAAA\     |  MM|--- | MM|   |  EEEE|          \  WW/  WW WW/  WW/    | OO|  |  OO|  |  NN\ NN NN|
                   |  GG   \G|    /  AA/--\ AA\    |  MM|    | MM|   |  E|--/           \  WW WW\  WW WW/     \  OO_/  OO/   |  NN|\ NNNN|
                   |   GGGGGG|   /  AA/    \ AA\   |  MM|    | MM|   |  EEEEEE|          \  WWW/ \  WWW/       \  OOOOOO/    |  NN| \ NNN|
                    \-------/   /____/      \___\   \__/      \_/     \______/            \___/   \___/         \______/      \__/   \__/
                      """)  # prints the string
            break   #reset the game

        if(counter == 7):   # it counts the steps until you get to the step 7 so it can print Game Over
            print("""
                      _______          ___          ____     ____     ________        ________    _____       _____    ________     ________
                    /  GGGGGG|        /  A\        |  MM|   /  MM|   |  EEEEEE|      /  OOOOOO\   \  VV\     /  VV/   |  EEEEEE|   |  RRRRRR\   
                   |  GG             /  AAA\       |  MMMM|/ MMMM|   |  E|---/      /  OO-\  OO\   \  VV\   /  VV/    |  E|---/    |  RR|\ RR|
                   |  GG   __       /  A   A\      |  MM MMMMM MM|   |  EEEE|       | OO|  |  OO|   \  VV\ /  VV/     |  EEEE|     |  RR|/ RR|
                   |  GG  |GG|     /  AAAAAAA\     |  MM|--- | MM|   |  EEEE|       | OO|  |  OO|    \  VV/  VV/      |  EEEE|     |  RRRRR<
                   |  GG   \G|    /  AA/--\ AA\    |  MM|    | MM|   |  E|--/       \  OO_ / OO/      \  VV/VV/       |  E|--/     |  RR\ RR\  
                   |   GGGGGG|   /  AA/    \ AA\   |  MM|    | MM|   |  EEEEEE|      \  OOOOOO/        \  VVV/        |  EEEEEE|   |  RR|\ RR|
                    \_______/   /____/      \___\   \__/      \_/     \______/        \______/          \___/          \______/     \__/  \_/
                    """)  # prints the string
            print(f"The word was= {myFood}") # prints the correct word that you were looking for
            break   #reset the game
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

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
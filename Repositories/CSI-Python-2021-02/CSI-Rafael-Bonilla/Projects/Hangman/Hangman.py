import json, ssl
import urllib.request
from Color import Color

def getColor():
# This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
    colorURL = "https://random-data-api.com/api/color/random_color"

# Execute HTTP Request
    req = urllib.request.Request(colorURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

# It enables the objects in the class Color to be used in this code
    color:Color = Color(**requestData)
    return color.color_name.upper()

# my_List is a list that compiles all of the letters used, no matter if it was correct or not.
my_List = [""]

# variable "steps" is the amount of steps that there are for the game.
steps = ["""
    +----------------+
    |                |
    |
    |
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    | 
    |
    |
    |
    |
    |
    \__________________""", 
    """
    +----------------+
    |                |
    |              👁👄👁
    |                |
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    |               /|
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    |               /|\\
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    |               /|\\
    |               / 
    |
    |
    |
    |
    \__________________""",
     """
    +----------------+
    |                |
    |               X👄X
    |               /|\\
    |               / \\
    |
    |
    |
    |
    \__________________"""]
# print(steps[0])

#print (color.color_name)

# it prints the amount of letters in the word in underscores, _.
# print (len(color.color_name)* " _")

# It validates if the letter chosen is under one character and if it as a letter.
def input_function():
    while(True):
        letter = input("Choose letters to guess a word related to a color ").upper()

        special_characters = "!@#$%^&*()-+?_=,<>/"
        
# It invalidates the inputs that are more than 1 character, is a digit, is a space, is a special character, 
# and is a letter that was already used by the past player.
        if(len(letter)!= 1):
            print("ERROR input a letter, no more than one character")
            continue
        if (letter.isdigit()):
            print("ERROR input a letter, not a digit")
            continue
        if (letter.isspace()):
            print (("ERROR input a letter, not a space"))
            continue
        if  (letter in special_characters):
            print("ERROR input a letter, not a special character")
            continue
        if (letter in my_List):
            print ("ERROR input a letter, letter already used try another letter that you have not used")
            continue
        my_List.append(letter)
        return letter

# print(input_function())

# This function that prints the word in underscores. While the with the player adds characters, it changes
# the underscore into the letter added or if it is not a character in the word then if it was not a part of 
# the letters in the word then it stays as an underscore. 
def printword (color):
    Temp:str=""
    for letter in color:
# It replaces the underscore into the letter that the player inputed correctly
        if letter in my_List:
            Temp+= letter
# If the letter inputed by the player is incorrect, than it keeps it as an underscore
        else: 
            Temp+="_"
# I the letter is the same as the color, then the player won.
        if Temp == color:
            print("CONGRATS, NOW YOU ARE A COLOR CONNOISSEUR!!!")
            break
    print (Temp)

# Every time it runs, it detects if a letter that was not in the color name and adds +1 to the amount of errors.
def getErrors(color):
    error = 0
# It adds an error into the variable "error" if the inputed letter is not in the chosen word.
    for letter in my_List:
        if (letter not in color):
            error += 1
        
    return error

# After the player answers the first letter, the game restarts all of the functions that are needed to run 
# the game to be able to input the next letter.
while (True):
    color = getColor() 
    # error = getErrors(color)
# It prints the current step of the game according to how many errors the player had.
    while (True):
        error = getErrors(color)
        print (steps[error])
        printword(color)
# When the variable "error" reach 6 it states to the player that it was a game over and restarts the game.
        if error == 6:
            print(f"GAME OVER, you absolute buffoon the word was {color}")
            my_List = [""]
            print("-------------------------------------------")
            break

        input_function()
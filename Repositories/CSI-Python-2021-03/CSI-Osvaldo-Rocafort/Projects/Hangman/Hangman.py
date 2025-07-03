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
    

    
    
    
        
        
        
    
    
    
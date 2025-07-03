# Hangman Rubric: CSI-Francisco-Ruiz

## Score: 90/100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 | 30 | 
| random word               | 5  | 5 | 
| multiline string array    | 5  | 5 | 
| Validate input            | 15 | 15 | 
| Find matches              | 10 | 10 | 
| Display the current step  | 10 | 10 | 
| Display attempted letters | 10 | 0 | 
| game progression          | 10 | 10 | 
| restart game              | 5  | 5 | 

<br>

### Submitted Work: 

```python


import json, ssl
from random import Random
import string
import urllib.request
from RandomCryptoCoin import RandomCryptoCoin

#DISCLAIMER: This code might take some time to load at first, as well as take time to restart.

#RULES: A Hangman game will be presented to you, and the goal is to slowly type letters until you are able to figure out which word (crypto) is the true one. If a correct letter is typed, the hangman will remain static. If an incorrect letter is typed, the hangman will slowly be hung limb by limb, so be careful. 

#NOTES: If you win, the restart will work as intended, but for some reason whenever the hangman reaches the final stage in his execution, it doesn't end. So in order for it to end properly in a losing situation, you shall have to type an extra letter for it to proceed as normal. 

#This code prevents error, although it is not recommended to use or necessary.

ssl._create_default_https_context = ssl._create_unverified_context

#Here I create a function in order to acquire my word from random data in an api. I first start the function by using def, declaring the function. I then simply added getWord as a function name and then I added the parenthesis, and closed it with a colon. 

def getWord():

    #I print a string with a message that says "Fetching Crypto Coin", to let the user know that the code is working but that the hangman hasn't appeared yet and that the crypto is being fetched. It will repeat any time a new game is started, wether it be a game that was won or a lost game.

    print("Fetching Crypto Coin...")

    #Here I create a variable, calling it cryptocoinLink, as its definition is the very link from which I will be calling a respective crypto coin from. The link is the random data in an api that I mentioned earlier.

    cryptocoinLink = "https://random-data-api.com/api/crypto_coin/random_crypto_coin"

    #I create another variable yet again, this time for a urllib request. In essence, I request the URL from the variable I had created earlier, cryptocoinLink, all whilst naming the variable request.

    request = urllib.request.Request(cryptocoinLink)

    #Furthermore, I create a new variable called requestWord. With it, I use json to load the urllib request and open the url, effectively making it "read" all that is written in the website. 

    requestWord= json.loads(urllib.request.urlopen(request).read())

    #Yet again, I have created another variable, this time I call it present_coin, alluding to the fact that it is the current crypto coin I am using, not just any. And after my previous line of code "read" the website, it already knows that RandomCryptoCoin exists and I then request a word from inside the RandomCryptoCoin.

    present_coin = RandomCryptoCoin(**requestWord)

    #Then I return the present_coin along with its name. I achieve this by using the present_coin variable and appending it with .coin_name, which is a variable in the random crypto coin api. I also use .upper() so that it returns my coin in uppercase.
    
    return present_coin.coin_name.upper()



#Here I create a yet another variable with the name Steps. Its definition consists of a multiline string array that contains each and every step to my hangman. Not the game, but hangman itself, with my goal being that after every wrong answer, the steps would increase by 1.

Steps = ["""
        |____________|
        |            |
        |
        |
        |
        |
        |_____________

        """,
        """
        |____________|
        |            |
        |            O
        |
        |
        |
        |_____________          
        """,
        """
        |____________|
        |            |
        |            O
        |            |
        |
        |
        |_____________

        """,
        """
        |____________|
        |            |
        |            O
        |            |\\
        |
        |
        |_____________
        """,
        """
        |____________|
        |            |
        |            O
        |          //|\\
        |
        |
        |_____________
        """,
        """
        |____________|
        |            |
        |            O
        |          //|\\
        |          //
        |
        |_____________
        """,
        """
        |____________|
        |            |
        |            O
        |          //|\\
        |          // \\
        |
        |_____________
        """
]

#Now I create a variable called Incorrect_Integers so that I can store in a list all the possible numbers that could and shouldn't be used in the hangman game. 

Incorrect_integers = ["0","1","2","3","4","5","6","7","8","9"]

#I create a new variable with the same premise as the one before it, this time with symbols and it's called Incorrect_characters. 

Incorrect_characters = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","[","{","]","}","\\","|",";",":",",","<",">","/","?"]

#I create another variable called UsedLetters and it's purpose is to start as an empty list that will then be filled up later with used letters as the hangman game progresses. 

UsedLetters = []

#I create another function, this time called getInput. I define it the same way as I defined my first function, however this function's purpose is different, as I use while and if else logic. 

def getInput():

    #Here I use while logic, creating a loop. 

    while(True):

        #I create yet another variable, this time called letter. It equates to an input which contains a string and .upper() at the end so that it gets capitalized.

        letter = input("Type a letter of your choice, be wary, as a wrong letter will cost you:").upper()
    
        #Here I use if else logic, and in this particular line I use len, which returns the length of my variable letter. If the length of my letter is 1, it continues. 

        if (len(letter) !=1):
            continue

        #Here I simply use if else logic to determine if the letter is actually a symbol by making it check inside of the list I had created earlier. 

        if letter in Incorrect_characters:

            #After that, I make it print a string to let the user know that they can't use special characters in a non-offensive manner, then I continue. 

            print("No puedes usar special characters, un bofetón")
            continue
        
        #I do the same but with the list Incorrect_integers instead.

        if letter in Incorrect_integers:

            #I let the user know again, that they might not use numbers in a non-offensive manner, by printing a nice string for them. I continue.

            print("No puedes usar integers, un bofetón")
            continue
        
        #I apply the same logic yet again for the UsedLetters variable. 

        if letter in UsedLetters:

            #I also apply another string that includes a nice message for the user. I continue the loop.

            print("Ya usaste esta, un bofetón")
            continue

        #Now I put my empty UsedLetters list to good use by using .append right after it and by appending the letter variable which I had defined earlier. This works because it doesn't rewrite the whole list, but rather modifies it letter after letter. 

        UsedLetters.append(letter)

        #I return the letter.

        return letter

#I create a new function. I use def, name the function printword, and include the parameter myWord inside the parenthesis followed by a colon. 

def printword(myWord):

    #I create another variable called temp. In it is a string object which consists of an empty string. 

    Temp:str = ""

    #I use for logic for every letter(variable) in the variable myWord and I end it with a colon.

    for letter in myWord:

        #Using if logic, I determine whether the letter typed is in the list inside the variable UsedLetters.

        if letter in UsedLetters:

            #Now I use the variable Temp to add and asign the variable letter.
            
            Temp += letter

        #I implement else logic.

        else:

            #After using else, I used the variable Temp to add and asign an undescore inside of a string. 

            Temp += "_"

    #I return the variable Temp.

    return Temp

#I create another function with play as its name; it's purpose is to be used everytime after a game is ended, in order to restart the game. The rest of the code is at the end. 

def play():

    #I create a variable called myWord which equated to the getWord function with .upper() assigned next to it, to ensure that all letters in my word or crypto coin are in upper case. .upper() works by returning a copy of the string in uppercase. 

    myWord = getWord().upper()

    #I create a new variable called stages. It's definition is an integer, 0. I plan to add a stage for each of the steps I created inside the steps list. Afterwards, it will reset to 0 whenever a new game is started.

    stages = 0
    

    #I create another loop using while logic.

    while True:

        #I print the variable steps as well as stages. 

        print (Steps[stages])

        #I use temp as a variable again, this time equating to my function printword and the variable myWord.

        temp = printword(myWord)

        #I print the variable temp.

        print(temp)

        #Using if logic, the parameters next to if include my temp variable if it equated to the myWord variable. 

        if(temp == myWord):

            #For this hypothetical situation, I print a string with a warm-hearted message for the user if they won. 

            print("Ganaste, no importa, un bofetón")

            #I break out of the loop.

            break

        #I define the variable letter again, this time with the function getInput and the suffix .upper(), fulfilling the same purpose as earlier, to return a copy uppercased. 

        letter =  getInput().upper()

        #I create a new if statement; including a situation in which the variable letter is not in the variable myWord.

        if  letter not in myWord:

            #I define stages again, this time by making it equal the earlier definition of stages, an integer(0), and add 1 to it. 

            stages = stages +1

            #In my final if statement, I include a situation where stages == 7.

            if stages == 7:

                #I print a final string with a nice message for the user just in case they weren't able to figure out what the mystery crypto was.

                print("Perdiste, un bofetón")

                #I break out of the loop.

                break

#I use while logic to create another loop, in order to restart the game. 

while True:

    #I use the function play that I had defined earlier. This basically makes getWord happen again and resets the stages to 0. 

    play()

    #I define UsedLetters by creating a new empty list for every time a new game is started. 

    UsedLetters = []
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
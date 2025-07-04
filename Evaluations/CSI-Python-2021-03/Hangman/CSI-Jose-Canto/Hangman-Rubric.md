# Hangman Rubric: CSI-Jose-Canto

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
| game progression          | 10 | 10 | 
| restart game              | 5  | 4 | 

<br>

### Submitted Work: 

```python


import random


Steps = [
"""   _______
     |/      |
     |      
     |      
     |       
     |      
     |
     |___
""",
"""
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
     |___
""",

"""
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
     |___
""",
"""
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
     |___
""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___
""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___
""",
"""
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
     |___
"""
]

words = ["CELTICS", "BULLS", "CAVS", "BUCKS", "MAVERICKS", "WARRIORS", "LAKERS", "SPURS", "SIXERS", "CLIPPERS", "PISTONS", "KINGS", "NUGGETS", "HEAT", "SUNS", "NETS", "ROCKETS", "THUNDER", "JAZZ", "HAWKS"]

def get_Word(wordList):
     # This function returns a random string from the list of strings.
     #In this case, the computer will choose a random NBA Team
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

def display(missedLetters, correctLetters, compWord):       #This will display the users data 
     print(Steps[len(missedLetters)-1])                  #(guessed letters aswell as the word he is guessing)
                                            
     print("Used letters:", end=" ")         #add a space after each letter in the wrong guesses
     for letter in wrongLetters:
         print(letter, end=" ")
     print()

     blanks = "_" * len(compWord)       #This makes it so that there are equal amounts of blanks as their are letters in the word

     for i in range(len(compWord)): # Replace blanks with correctly guessed letters.
        if compWord[i] in correctLetters:
             blanks = blanks[:i] + compWord[i] + blanks[i+1:]    #the letter will be substituted in the blank

     for letter in blanks:          # Show the word with spaces in between each letter.
         print(letter, end=" ")
     print()

def getGuess(alreadyGuessed):
                                   # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
     while True:
         print("Guess a letter. Hint: NBA Teams")
         guess = input()
         guess = guess.upper()                         #This is the filter for the input
         if len(guess) != 1:                           #this will make sure that only the accepted asnweres go through
             print("Please enter ONE (1), letter.")
         elif guess in alreadyGuessed:
             print("You have already guessed that letter. Choose another one.")
         elif guess not in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z':
             print("Please enter a LETTER, (in british accent) you donut.")
         else:
             return guess

def playAgain():
     # This function returns True if the player wants to play again; otherwise, it returns False.
     #If True then the game will start again, if False the game will end.
     print("Do you want to play again? (YES or NO)")
     return input().upper().startswith("Y")

print("Hang Man!!")
wrongLetters = " "
correctLetters = " "
compWord = get_Word(words)         #compWord is the randomly selected string
gameIsDone = False

while True:
     display(wrongLetters, correctLetters, compWord) #This will show the user what letter he has used
     guess = getGuess(wrongLetters + correctLetters)

     if guess in compWord:                        #If the guess is in the random word then the gue sis a correct letter
         correctLetters = correctLetters + guess

         # This will check if the player has won.
         foundAllLetters = True
         for i in range(len(compWord)):
             if compWord[i] not in correctLetters:     
                 foundAllLetters = False          #this will loop everytime the user guesses a letter until he finds the word,
                 break                            #or runs out of lives
         if foundAllLetters:
             print("CORRECT! The word is " + compWord +
                   " You have won!!")            #if the player has found all the letters the game will end
             gameIsDone = True               #This code makes it so that if the user finds all the letters the game will be done
     else:                                   #making sure the game is done will then be used
         wrongLetters = wrongLetters + guess

         # Check if player has guessed too many times and lost.
         if len(wrongLetters) == len(Steps) - 1:
             display(wrongLetters, correctLetters, compWord)
             print("You ran out of guesses!\nAfter " +                
                   str(len(wrongLetters)) + " wrong guesses and " +     #If the player has lost this will print
                   str(len(correctLetters)) + " correct guesses",
                   "the word was " + compWord + "")
             gameIsDone = True               #This makes it so that the game is done, so that the user will be asked to play again

     # Ask the player if they want to play again (but only if the game is done).
     if gameIsDone:                #The code above will make sure that gameIsDone is true so that this code will strat
         if playAgain():
             wrongLetters = ""          #If the play again is true (answered YES) the code will run and re-start the game
             correctLetters = ""
             gameIsDone = False
             compWord = get_Word(words)
         else:
            print("Game Over")     #Prints game over if the return when asked if "you want to restart the game" is not YES
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
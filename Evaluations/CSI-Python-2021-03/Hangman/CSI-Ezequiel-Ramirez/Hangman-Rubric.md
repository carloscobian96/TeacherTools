# Hangman Rubric: CSI-Ezequiel-Ramirez

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
# The random package is very important for the code to work perfectly.

def getMeme(): 
    HangmanWordList = ["MEME", "MEMES", "DAT BOI", "SANIC", "WEEGEE", "I WONDER WHATS FOR DINNER", "YTP", "CRINGE", "FIDGET SPINNER", "DEAD MEME", "MLG", "AH YES THE FLOOR HERE IS MADE OF FLOOR", "GET REAL", "NYAN CAT", "WE ARE NUMBER ONE", "STEAMED HAMS", "DEEZ NUTZ", "GOTTEM GGS", "WE LIVE IN A-SOCIETY", "YOUR MOM GAY", "BRUH MOMENT", "MEGALOVANIA", "PEPE HANDS", "WHY ARE WE STILL HERE", "LIGMA BALLS", "BASED AND REDPILLED", "BIG SHOT", "HIT OR MISS"]
    return random.choice(HangmanWordList).upper()
    #The full list of words used for the game, with them all in upper case.

def Intro():
    Name = input("Welcome to Zeke's Epic Gamer Meme Hangman! Please enter your name so I can know if you're Based or Cringe: ")
    #Honestly, the whole name entry thing is kinda unnecessary, but it is pretty funny.
    if Name == "Based":
        print("""Wow, you really are Based! Well then Based Department, let's begin!
              My Meme Machine will randomly select a meme, be it a word or short phrase. 
              You will have to guess that dank meme by inputting its characters before the man gets hung.
              Don't feel too bad for him though, he plays Genshin Impact.""")
    else:
        print("What? Your name isn't the word Based written in this specific way? Now THAT's cringe. I don't want no normies in my Hangman, SCRAM!")
        exit()
        #Note: Yes Cobian, you cannot play if your name is not "Based". If you ran into this, that's simply a skill issue.

def PlayAgain():
    #This function's purpose is to trigger after the game ends and ask the user if they want to play again. Self-
    Prompt = input("Would you like to try another GAMER meme? Enter 'Y' for yes and literally anything else for no: ").upper()
    if Prompt == "Y":
        print("Alrighty then! Let's do this!")
        HangMeMan()
        #This if succesfully restarts the Hangman game.
        
    else:
        print("I am judging you intensely.")
        exit()
        #This else is for beta males who don't want to infinitely replay Hangman.

Intro()

def HangMeMan():
    Characters = "QWERTYUIOPASDFGHJKLZXCVBNM "
    SpecialCharacters = "!@#$%^&*()_+=`~;:[]{/?=}|<>,./1234567890"
    Meme = getMeme()
    CharactersGuessed = []
    Attempts = 6
    Guessed = False
    print()
    #These variables are going to be very important for the rest of the function, including the character list, the characters guessed, the amount of attempts, and more.
    
    def HungMan():
        if Attempts == 6:
            #Else-if for the visual of the Hung Man, with the determining factor being the amount of attempts.
            print("   +--------+")
            print("   |        |")
            print("   |         ")        
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
            #I previously used a multi-line string to do this, but the formatting was way off, so I changed it. Ckeck my previous commits if you want proof I guess.
        elif Attempts == 5:
            print("   +--------+")
            print("   |        |")
            print("   |        O ")        
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
        elif Attempts == 4:
            print("   +--------+")
            print("   |        |")
            print("   |        O ")        
            print("   |        | ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
        elif Attempts == 3:
            print("   +--------+")
            print("   |        |")
            print("   |        O ")        
            print("   |       -| ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
        elif Attempts == 2:
            print("   +--------+")
            print("   |        |")
            print("   |        O ")        
            print("   |       -|- ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
        elif Attempts == 1:
            print("   +--------+")
            print("   |        |")
            print("   |        O ")        
            print("   |       -|- ")
            print("   |       / ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
        else:
            print("   +--------+")
            print("   |        |")
            print("   |        O ")        
            print("   |       -|- ")
            print("   |       / /")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("___|______________")
            
    HungMan()
    print("The meme contains", len(Meme), "characters.")
    print(len(Meme) * "_")
    #String's that say the amount of characters in the meme, then visually represents it with underscores.
    
    while Guessed == False and Attempts > 0:
        #This is the bulk of the code that makes the magic happen.
        print("You have " + str(Attempts) + " attempts remaining.")
        #This string lists the remaining attempts.
        Guess = input("Try guessing a letter, inputting a space or, if you're feeling lucky, try to guess the whole phrase: ").upper()
        #The string which allows you to input your answer.
        
        if len(Guess) == 1:
            #This if statement is for attempts with one letter.
            if Guess in CharactersGuessed:
                print("You already tried that letter, you silly little STOOPID BOY!")
                #This is for stupid idiot babies with a lack ofobject permanence. Oh, and for characters they already tried I guess.
            elif Guess in SpecialCharacters:
                print("I said to input a letter, not whatever that is!")
                #This is the preventative measure for special characters.
            elif Guess not in Meme:
                Attempts -= 1
                HungMan()
                print("Oops! That letter is not in the dank meme of choice.")
                CharactersGuessed.append(Guess)
                print(CharactersGuessed)
                #This is for characters not in the meme. Very cool and interesting, I know.
            elif Guess in Meme:
                HungMan()
                print("Poggers! That letter is in the meme!")
                CharactersGuessed.append(Guess)
                print(CharactersGuessed)
                #This is for gamers who get a character correct.
            else:
                print("Dude what the hell did you do get this???")
                #A really good question for something going horribly wrong.
        
        elif len(Guess) == len(Meme):
            #This elif is for attempts that guess the whole meme.
            if Guess == Meme:
                #The correct guess for big brained dudes.
                print("PogChamp! You got got the meme correctly! :)")
                Guessed = True
                PlayAgain()
            else:
                Attempts -= 1
                HungMan()
                print("Congratulations, you got the meme WRONG! You absolute baffoon! >:)")
                #This is what plays if the user becomes the loser and sucks ass... ASPIRATIONS IN LIFE I MEAN
        
        else:
            Attempts -= 1
            HungMan()
            print("Bruh, the length of what you entered is not the same as the meme. -1 attempts for being STOOPID.")
            #This last else statement basically just removes an attempt for typing something that isn't one character or the length of the word.
        
        MemeStatus = ""
        #This is basically the status of meme in solving it at any given point in time.
        
        if Guessed == False:
            #Guessed will always by default remain in false until the conditions of the else-if are met.
            for Characters in Meme:
                if Characters in CharactersGuessed:
                    MemeStatus += Characters
                else:
                    MemeStatus += "_"
                    #This else-if is supposed to replace any underscores that represent characters guessed with the characters themselves. I pray to God this works lmao.
            print(MemeStatus)
        
        if MemeStatus == Meme:
            print("PogChamp! You got got the meme correctly! :)")
            Guessed == True
            PlayAgain()
            #This if statement is basically the win condition, which then proceeds to initiate the function to play again.
        elif Attempts == 0:
            HungMan()
            print("Imagine running out of attempts and losing the game. Literally could not be me.")
            PlayAgain()
            #Meanwhile, this elif is the lose condition, again activating the restart function.

HangMeMan()
#This just runs the code in the function, pretty self-explanatory.
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
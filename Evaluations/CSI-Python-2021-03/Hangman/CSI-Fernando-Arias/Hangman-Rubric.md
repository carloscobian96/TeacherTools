# Hangman Rubric: CSI-Fernando-Arias

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

#All words thats can be used in my hangman
word_list = ["CLUE", "LIFE", "JESUITA", "LOYOLA", "IGLESIA", "BUENOSAIRES", "BOGOTA", "QUITO", "LOOPS", "FAJARDO", "OROCOVIS", "ISABELA", "RINCON", "GURABO", "PONCE", "BAYAMON", "CAYEY", "MONOPOLIO", "STRING", "LIST", "FLOAT", "ARECIBO", "DORADO", "LUQUILLO"]
#Every step in hangman
def display_hangman(tries):
    steps = ['''
     |---|
     O   |
    /|\  |
     /\  |
        ===''', '''
     |---|
     O   |
    /|\  |
      \  |
       ===''', '''
    |---|
    O   |
   /|\  |
        |
       ===''', '''
    |---|
    O   |
   /|   |
        |
       ===''', '''
    |---|
    O   |
    |   |
        |
       ===''', '''
    |---|
    O   |
        |
        |
       ===''', '''
    |---|
        |
        |
        |
       ===''']

    return steps[tries]

#This code is to select a random word from my word list
def getWord(word_list):
    word = random.choice(word_list)
    return word.upper()
#This is a list of the letters the user cant use
incompleteLetters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

#This code is going to print an error if the user selects a letter thats is in my list of incomplete letters and going to make it a upper case letter.
def getInput():
   Letter = input("Select letter")
   while(Letter.upper() not in incompleteLetters):
      print("Error")
#To start playing
def play(word):
    word_completion = "_" * len(word) #This will show me the amount of spaces the letter chosen has
    guessed = False
    guessed_letters = []#This stores the guessed letters
    guessed_words = []
    tries = 6 #amount of tries to guess the word chosen
    print("Lets play Hangman")
    print("No use of lowercase, must be Upper Case letters always.")
    print(display_hangman(tries))#Print the steps so you see how much tries you have left 
    print(word_completion)#prints the spaces of the letter
    print("\n")
    #Here I created a boolean logic that will make the game know if the letter that the user inserted is correct or incorrect
    while not guessed and tries > 0:
        guess = input("Guess the word: ").upper() 
        if len(guess) == 1 and guess.isalpha(): 
            #This if elif will make the game tell the user if the word he just inserted has been used before or it is incorrect 
            # and will add a step
            if guess in guessed_letters:
                print("Already used that letter", guess, "!")
            elif guess not in word:
                print(guess, "Not in the word")     
                tries -= 1                     #This adds another step to the hangman so it takes away a try.
                guessed_letters.append(guess)
            else:                                                   
                #This else is for when the user inserted a letter if it is not incorrect nor already used the it will be in the word selected
                print("Yes", guess, "that letter is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess] #Changes each string to a list of numbers starting with 0 that will match the index of steps
                for index in indexes:
                    word_as_list[index] = guess 
                word_completion = "".join(word_as_list)
                if "_" not in word_completion: #If the letter substitutes the underscore it means that it is true
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guessed in guessed_words:   #If the user choose a letter he already used it will tell him that it was already used and he can select another letter without priting the next step.
                print("Already tried that", guess,)
            elif guess != word:  #The user guessed incorrectly and it will print the next step
                print(guess, "Not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input")
        print(display_hangman(tries)) #This will print the hangman steps so the user can see his progress
        print(word_completion) #Prints the amount of characters the word selected has.
        print(guessed_letters)#This will make the letters the user has guessed seen.
        print("\n")
    #I use an if else that tells me either you got the correct word or you ran out of opportunities to guess the word.
    if guessed:
        print("You got the word correct")
    else: 
        print("No more tries left. The correct word"+word+" Better luck next time.")
                
    #This code will offer the user playing the game if he wants to restart the game or not.
def main():
    word = getWord(word_list)
    play(word)
    while input("Go again (Yes/No)").upper() == "Y":
        word = getWord(word_list)  #This will choose a new word from my word list if the user decides to go again.
        play(word)

    print("Game Over")#If you put anything other than Y it will print game over
if __name__ == "__main__":
    main() 
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
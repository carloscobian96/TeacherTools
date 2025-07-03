Yourpick = input("Let's play Rock, Paper, Scissors! Select your pick:")
print (f"You selected: {Yourpick}")

# Ask the user to select their pick for rock, paper, scissors so that the program may resume.
# It is important that you don't show the computer's response first so that the program functions like the typical rock, paper, scissors game.

import random

foo = ['Rock', 'Paper', 'Scissors']
Computerchoice = random.choice(foo)
print (f"Computer selected: {Computerchoice}")

# The computer's choice is random, as one would choose in any game like this.
# Make sure that your results factor in your choice, even if they were spelled with Capital uppercase or lowercase. 
# It's not indispensable or anything but it helps making a more comfortable experience for the user that accomodates itself to their liking. 

if Yourpick == 'Rock' or 'rock' and Computerchoice == 'Rock':
    print ("Tie!")
elif Yourpick == 'Rock' or 'rock' and Computerchoice == 'Paper':
    print ("I win!")
elif Yourpick == 'Rock' or 'rock' and Computerchoice == 'Scissors':
    print ("You win!")
elif Yourpick == 'Paper' or 'paper' and Computerchoice == 'Paper':
    print ("Tie!")
elif Yourpick == 'Paper' or 'paper' and Computerchoice == 'Scissors':
    print ("I win!")    
elif Yourpick == 'Paper' or 'paper' and Computerchoice == 'Rock':
    print ("You win!")
elif Yourpick == 'Scissors' or 'scissors' and Computerchoice == 'Scissors':
    print ("Tie!")
elif Yourpick == 'Scissors' or 'scissors' and Computerchoice == 'Rock':
    print ("I win!")
elif Yourpick == 'Scissors' or 'scissors' and Computerchoice == 'Paper':
    print ("You win!")

# Provide a result for each possible outcome in this game involving your three choices. 
# It will either result in victory, defeat, or tie depending on which item you enter. 
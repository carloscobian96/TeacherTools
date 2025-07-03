import random

PlayerChoice = input("Want to test your skills against the computerr?, lets play rock paper scissors! Choose one: rock, paper, or scissors ")
print(PlayerChoice)

RPS = ['rock', 'paper', 'scissors']

computerChoice = random.choice(RPS)
print(f"Computer selected: {computerChoice}")
print(f"Player selected: {PlayerChoice}")

# now that we have defined variables and functions, we will now tell the computer how to act on the player's answers

#so i dont have to repeat very similar programs, i wrote one where if the player chooses the same answer as the computer, they tie
if(PlayerChoice == computerChoice):
    print("You tied :/")

# here i programed the three ways the player can win
elif(PlayerChoice == 'rock' and computerChoice == "scissors"):
    print('You won! :)')

elif(PlayerChoice == 'paper' and computerChoice == "rock"):
    print('You won! :)')

elif(PlayerChoice == 'scissors' and computerChoice == "paper"):
    print('You won! :)')

#here i programmed the three ways the player can loose
elif(PlayerChoice == 'rock' and computerChoice == "paper"):
    print('You lost :(')

elif(PlayerChoice == 'paper' and computerChoice == "scissors"):
    print('You lost :(')

elif(PlayerChoice == 'scissors' and computerChoice == "rock"):
    print('You lost :(')

#just in case the player commits a typo or there is an error, i wrote this code
else:print("Something isnt right, maybe try again?")
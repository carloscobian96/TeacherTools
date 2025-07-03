import random

Choose = ["Rock", "Paper", "Scissor"]

#The AI chooses something random
computerChoice = random.choice(Choose)
userChoice = input ("What do you play: rock, paper or scissor?")
print(f"User selected: {userChoice}")
print(f"Computer selected: {computerChoice}")

if (computerChoice == userChoice):
    print("Tied")
    
if (userChoice == "Rock" and computerChoice == "Paper"):
    print("You lose")

if (userChoice == "Scissor" and computerChoice == "Paper"):
    print("You win")

if (userChoice == "Rock" and computerChoice == "Scissor"):
    print("You win")

if (userChoice == "Paper" and computerChoice == "Rock"):
    print("You win")
if (userChoice == "Paper" and computerChoice == "Scissor"):
    print("You lose")
if (userChoice == "Scissor" and computerChoice == "Rock"):
    print("You lose")







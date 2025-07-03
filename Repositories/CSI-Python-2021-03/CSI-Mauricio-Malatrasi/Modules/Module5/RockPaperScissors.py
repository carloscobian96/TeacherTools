import random

MyChoice = input("rock, paper or scissors")
print(MyChoice)

computerChoice = ["rock", "paper", "scissors"]
computerChoice = random.choice(computerChoice)
print(f"Computer chose: {computerChoice}")

# Based on what the computer chose, who wins

if(MyChoice == computerChoice):
    print("Tie")
elif(MyChoice == "rock" and computerChoice == "scissors"):
    print("You won!")
elif(MyChoice == "rock" and computerChoice == "paper"):
    print("Computer won!")
elif(MyChoice == "paper" and computerChoice == "rock"):
    print("You won!")
elif(MyChoice == "paper" and computerChoice == "scissors"):
    print("You lost!")
elif(MyChoice == "scissors" and computerChoice == "paper"):
    print("You won!")
elif(MyChoice == "scissors" and computerChoice == "rock"):
    print("You lost!")
else:
    print("Oops! something went wrong.")
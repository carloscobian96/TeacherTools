import random

foo = ["Rock", "Paper", "Scissors"]
computerChoice = random.choice(foo)
userChoice = input("select Rock, Paper or Scissors ")
print(computerChoice)

if(userChoice == "Rock" and computerChoice == "Paper"):
    print("You lose")
elif(userChoice == "Rock" and computerChoice == "Scissors"):
    print("You win")
elif(userChoice == "Rock" and computerChoice == "Rock"):
    print("Tie")
elif(userChoice == "Paper" and computerChoice == "Scissors"):
    print("You lose")
elif(userChoice == "Paper" and computerChoice == "Paper"):
    print("Tie")
elif(userChoice == "Paper" and computerChoice == "Rock"):
    print("You win")
elif(userChoice == "Scissors" and computerChoice == "Rock"):
    print("You lose")
elif(userChoice == "Scissors" and computerChoice == "Scissors"):
    print("Tie")
elif(userChoice == "Scissors" and computerChoice == "Paper"):
    print("You win")
else:
    print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock")

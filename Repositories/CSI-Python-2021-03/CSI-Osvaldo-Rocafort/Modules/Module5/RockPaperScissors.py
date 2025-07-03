import random

mychoice = input("rock, paper, or scissors")
print(mychoice)

computerChoice = ("rock","paper","scissors")
Computerchoice = random.choice(computerChoice)
print(f"Computer selected: {Computerchoice}")

# Based on what the computer chose, who wins 

if(computerChoice == "rock" and mychoice == "rock"):
     print("tied")
elif(computerChoice == "scissors" and mychoice == "rock"):
     print("You win")
elif(computerChoice == "paper" and mychoice == "rock"):
     print("computerwon")
elif(computerChoice == "paper" and mychoice == "paper"):
    print("tied")
elif(computerChoice == "rock" and mychoice == "paper"):
    print("You win")
elif(computerChoice == "paper" and mychoice == "scissors"):
    print("You Win")
elif(computerChoice == "scissors" and mychoice == "scissors"):
    print("tied")
elif(computerChoice == "scissors" and mychoice == "paper"): 
    print("computerwon")
elif(computerChoice == "rock" and mychoice == "paper"):
    print("You win")
elif(computerChoice == "scissors" and mychoice == "rock"):
    print("You win")

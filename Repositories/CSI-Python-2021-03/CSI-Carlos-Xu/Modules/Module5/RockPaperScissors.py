import random
choices = ["rock", "paper", "scissors"]
PlayerChoice = input("Lets play! Choose one: rock, paper, or scissors.")
ComputerChoice = random.choice(choices)

print(f"Computer selected: {ComputerChoice}")
print(f"Player selected: {PlayerChoice}")


if(PlayerChoice == "rock" and ComputerChoice == "scissors"):
    print("Rock crushes scissors. You won!")
elif(PlayerChoice == "rock" and ComputerChoice == "paper"):
    print("You lost!")
elif(PlayerChoice == "rock" and ComputerChoice == "rock"):
    print("It's a tie!")
elif(PlayerChoice == "paper" and ComputerChoice == "rock"):
    print("You win!")
elif(PlayerChoice == "paper" and ComputerChoice == "scissors"):
    print("You lost!")
elif(PlayerChoice == "paper" and ComputerChoice == "paper"):
    print("It's a tie")
elif(PlayerChoice == "scissors" and ComputerChoice == "paper"):
    print("You win!")
elif(PlayerChoice == "scissors" and ComputerChoice == "rock"):
    print("You lost!")
elif(PlayerChoice == "scissors" and ComputerChoice == "scissors"):
    print("It's a tie")
else:
    print("Something isn't right, try again")

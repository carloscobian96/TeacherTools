import random

choices = ["rock", "paper", "scissors"]

MyChoice = input("What is your choice")
print(f"Computer select:{MyChoice})")

computerChoice = random.choice(choices)
print(f"Computer select:{computerChoice}")

if(computerChoice == MyChoice):
    print("tied")
elif(computerChoice == "scissors" and MyChoice == "rock"):
    print("i win")
elif(computerChoice == "rock" and MyChoice == "paper"):
    print("i win")
elif(computerChoice == "paper" and MyChoice == "scissors"):
    print("i win")
elif(computerChoice == "rock" and MyChoice == "scissors"):
    print("i lose")
elif(computerChoice == "paper" and MyChoice == "rock"):
    print("i lose")
elif(computerChoice == "scissors" and MyChoice == "rock"):
    print("i lose")
elif(computerChoice == "scissors" and MyChoice == "scissors"):
    print("tied")
elif(computerChoice == "rock" and MyChoice == "rock"):
    print("tied")
elif(computerChoice == "paper" and MyChoice == "paper"):
    print("tied")
else:
    print("Something went wrong")
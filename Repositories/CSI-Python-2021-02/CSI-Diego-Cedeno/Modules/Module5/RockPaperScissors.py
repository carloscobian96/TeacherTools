import random

foo = ["rock", "paper", "scissors"]
computerChoice = random.choice(foo)

userChoice = input("Enter your choice ")

print(f"Computer selected: {computerChoice}")
print(f"User selected: {userChoice}")

# Add logic below this line

if(userChoice == "rock" and computerChoice == "rock"):
    print(" its a tie ")
elif(userChoice == "rock" and computerChoice == "paper"):
    print(" you loose")
elif(userChoice == "rock" and computerChoice == "scissors"):
    print("you win")

elif(userChoice == "paper" and computerChoice == "paper"):
    print(" its a tie ")
elif(userChoice == "paper" and computerChoice == "scissors"):
    print(" scissors wins")
elif(userChoice == "paper" and computerChoice == "rock"):
    print("paper wins")

elif(userChoice == "scissors" and computerChoice == "scissors"):
    print(" its a tie ")
elif(userChoice == "scissors" and computerChoice == "paper"):
    print(" scissors wins")
elif(userChoice == "scissors" and computerChoice == "rock"):
    print("rock wins")








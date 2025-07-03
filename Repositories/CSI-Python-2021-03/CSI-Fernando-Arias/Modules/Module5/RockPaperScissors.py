import random

foo = ["rock", "paper", "scissors"]

myChoice = input("Choose rock, paper, scissors ")
print(f"I selected {myChoice}")

computerChoice = random.choice(foo)
print(f"Computer selected: {computerChoice}")


if(myChoice == foo[1] and computerChoice == foo[1]):
    print("You have tied")
elif(myChoice == foo[0] and computerChoice == foo[0]):
    print("You have tied")
elif(myChoice == foo[2] and computerChoice == foo[2]):
    print("You have tied")
elif(myChoice == foo[1] and computerChoice == foo[0]):
    print("You won")
elif(myChoice == foo[1] and computerChoice == foo[2]):
    print("You lost")
elif(myChoice == foo[2] and computerChoice == foo[0]):
    print("You lost")
elif(myChoice == foo[2] and computerChoice == foo[1]):
    print("You won")
elif(myChoice == foo[0] and computerChoice == foo[1]):
    print("You lost")
elif(myChoice == foo[0] and computerChoice == foo[2]):
    print("You won")
else:
    print("You wrote something wrong ")
    





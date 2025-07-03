import random

items = ["rock", "paper", "scissors"]

myChoice = input("Choose: rock, paper or scissors ")
print(f"I selected {myChoice}")

compChoice = random.choice(items)
print(f"Computer selected: {compChoice}.")



if(myChoice == items[0] and compChoice == items[0]):
    print("You have tied, try again")
elif(myChoice == items[1] and compChoice == items[1]):
    print("You have tied, try again")
elif(myChoice == items[2] and compChoice == items[2]):
    print("You have tied, try again")
elif(myChoice == items[0] and compChoice == items[2]):
    print("CONGRADULATIONS! You beat the computer")
elif(myChoice == items[2] and compChoice == items[0]):
    print("O noo, you lost, try again.")
elif(myChoice == items[1] and compChoice == items[2]):
    print("O noo the computer has beaten you, try again.")
elif(myChoice == items[2] and compChoice == items[1]):
    print("CONGRADULATIONS! You beat the computer")
elif(myChoice == items[0] and compChoice == items[1]):
    print("The computer has beaten you, try again.")
elif(myChoice == items[1] and compChoice == items[0]):
    print("CONGRADULATIONS! You beat the computer")
else:
    print("You wrote something incorrect")

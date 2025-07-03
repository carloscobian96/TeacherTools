import random

MyChoice = input("Rock, Paper or Scissors")

computerChoice = ["Rock", "Paper", "Scissors"]
computerChoice = random.choice(computerChoice)
print(f"Computer selected: {computerChoice}")
print(f"I selected: {MyChoice}")

if(MyChoice == "Rock" and computerChoice== "Rock"):
    print("It is a tie")
elif(MyChoice == "Paper" and computerChoice== "Paper"):
    print("It is a tie")
elif(MyChoice == "Paper" and computerChoice== "Paper"):
    print("It is a tie")

elif(MyChoice == "Rock" and computerChoice== "Paper"):
    print("You lose!")
elif(MyChoice == "Rock" and computerChoice== "Scissors"):
    print("You just won!")

elif(MyChoice == "Paper" and computerChoice== "Rock"):
    print("You just won!")
elif(MyChoice == "Paper" and computerChoice== "Scissors"):
    print("You lose!")

elif(MyChoice == "Scissors" and computerChoice== "Rock"):
    print("You lose!")
elif(MyChoice == "Scissors" and computerChoice== "Paper"):
    print("You just won!")

else:
    print("Something is not working")
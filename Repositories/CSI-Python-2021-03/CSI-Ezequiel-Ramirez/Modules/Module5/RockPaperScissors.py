import random

MyChoice = input("Let's play Rock, Paper, Scissors! What is your choice? ")

RPS = ["Rock", "Paper", "Scissors"]
computerChoice = random.choice(RPS)

if(MyChoice == "Rock"):
    if(computerChoice == "Rock"):
        print("I chose rock! We tied!")
    elif(computerChoice == "Paper"):
        print("I chose paper! You lose!")
    elif(computerChoice == "Scissors"):
        print("I chose scissors! You win!")

elif(MyChoice == "Paper"):
    if(computerChoice == "Rock"):
        print("I chose rock! You win!")
    elif(computerChoice == "Paper"):
        print("I chose paper! We tied!")
    elif(computerChoice == "Scissors"):
        print("I chose scissors! You lose!")

elif(MyChoice == "Scissors"):
    if(computerChoice == "Rock"):
        print("I chose rock! You lose!")
    elif(computerChoice == "Paper"):
        print("I chose paper! You win!")
    elif(computerChoice == "Scissors"):
        print("I chose scissors! We tied!")

else:
    print("That's not a valid choice!")
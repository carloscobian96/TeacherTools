import random

Options = ['Rock', 'Paper', 'Scissors']
computerChoice = random.choice(Options)
Userchoice = input("Selct your option") 
print(f"User selected: {Userchoice}")
print(f"Computerselected: {computerChoice}")

# Add logic below this line
if(Userchoice == "Paper" and computerChoice == "Rock"):
    print("You win")
elif(Userchoice == "Paper" and computerChoice == "Scissors"):
    print("You lose")
elif(Userchoice == "Paper" and computerChoice == "Paper"):
    print("Is a tie")
elif(Userchoice == "Rock" and computerChoice == "Rock"):
    print("Is a tie")
elif(Userchoice == "Rock" and computerChoice == "Scissors"):
    print("You win")
elif(Userchoice == "Rock" and computerChoice == "Paper"):
    print("You lose")
elif(Userchoice == "Scissors" and computerChoice == "Rock"):
    print("You lose")
elif(Userchoice == "Scissors" and computerChoice == "Paper"):
    print("You win")
elif(Userchoice == "Scissors" and computerChoice == "Scissors"):
    print("Is a tie")
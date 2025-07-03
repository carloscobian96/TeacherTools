import random
choice = ["rock", "paper", "scissor"]
computerChoice = random.choice(choice)
print("Make a choice between rock, paper or scissor...")
myChoice = input()

x = computerChoice
y = myChoice

if(x == y):
    print("It was a draw!")
elif(x == "rock", y == "paper" ):
    print("The Computer wins!")
elif(x == "rock", y == "scissor"):
    print("The Player wins!")
elif(x == "scissor", y == "paper"):
    print("The Player wins!")
elif(x == "scissor", y == "rock"):
    print("The Computer wins!")
elif(x == "paper", y == "rock"):
    print("The Player wins!")
elif(x == "paper", y == "scissor"):
    print("The Computer wins!")
else:
    print("The game was not able to decide on a winner due to an error...")

print(f"The computer chose: {computerChoice}")
print(f"You chose: {myChoice}")


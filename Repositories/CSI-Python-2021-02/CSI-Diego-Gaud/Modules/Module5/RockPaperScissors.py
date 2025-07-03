import random
options = ['Rock', 'Paper', 'Scissors']
computerChoice = random.choice(options)
userChoice = input("Choose a option to play")
print(f"User selected: {userChoice}")
print(f"Computer selected: {computerChoice}")

if(userChoice==computerChoice):
    print("its a tie")
if(userChoice=='Rock' and computerChoice=='Paper'):
    print("You lose")
if(userChoice=='Rock' and computerChoice=='Scissors'):
    print("You win")
if(userChoice=='Paper' and computerChoice=='Rock'):
    print("You win")
if(userChoice=='Paper' and computerChoice=='Scissors'):
    print("You lose")
if(userChoice=='Scissors' and computerChoice=='Paper'):
    print("You win")
if(userChoice=='Scissors' and computerChoice=='Rock'):
    print("You lose")


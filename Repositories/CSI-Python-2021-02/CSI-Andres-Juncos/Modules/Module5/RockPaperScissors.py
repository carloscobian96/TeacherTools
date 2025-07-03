import random

userchoice = input("What is your choice?")

foo = ['Rock', 'Paper', 'Scissors']
computerChoice = random.choice(foo)
print(f"Computer selected: {computerChoice}")


if(userchoice == computerChoice):
    print("Its a tie")
elif(userchoice=='Rock' and computerChoice=='Scissors'):
    print("User won!")
elif(userchoice=='Paper'and computerChoice=='Rock'):
    print("User won!")
elif(userchoice=='Scissors' and computerChoice=='Paper'):
    print("User won!")
elif(userchoice=='Paper' and computerChoice=='Scissors'):
    print("Computer won!")
elif(userchoice=='Scissors' and computerChoice=='Rock'):
    print("Computer won!")
elif(userchoice=='Rock' and computerChoice=='Paper'):
    print("Computer won!")



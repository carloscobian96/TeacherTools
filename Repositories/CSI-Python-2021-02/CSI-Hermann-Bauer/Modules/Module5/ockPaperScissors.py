import random
def game(p, c):
    try:
        print(f"You have {str(p)} points, the computer has {str(c)}")
        #ARRAY OF CHOICES
        moves = ["rock", "paper", "scissors"]
        #TAKES INPUT CONVERTS IT TO INDEX
        humanChoice = moves.index(input("rock, paper, scissors? "))
        #RANDOM INT AS CHOICE
        computerChoice = random.randint(0,2)
        print(f"Computer selected: {moves[computerChoice]}")
        #ROCKPAPERSCISSOR GAME LOGIC
        if(humanChoice == computerChoice):
            print("Tie")
        elif(humanChoice == 0 and computerChoice==2):
            print("you won")
            print(f"{moves[humanChoice]} beats {moves[computerChoice]}")
            p+=1
        elif(humanChoice == 1 and computerChoice==0):
            print("you won")
            print(f"{moves[humanChoice]} beats {moves[computerChoice]}")
            p+=1
        elif(humanChoice == 2 and computerChoice==1):
            print("you won")
            print(f"{moves[humanChoice]} beats {moves[computerChoice]}")
            p+=1
        else:
            print("you lost")
            print(f"{moves[humanChoice]} looses to {moves[computerChoice]}")
            c+=1
        game(p, c)
    except:
        print("Please input \"rock\", \"paper\" or \"scissors\"")
        game(p, c)

game(0,0)

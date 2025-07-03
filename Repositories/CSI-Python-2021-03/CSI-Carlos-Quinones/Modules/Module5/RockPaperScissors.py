import random

possibleWepons=["Rock","Paper", "Scissor"]
pcWeponChoice = random.choice(possibleWepons)
myWeponChoice = input("Rock Paper or Scissor, which one will you shoot? ")
def won():
    print(f"You won!!, the PC used {pcWeponChoice}")
def lost():
    print(f"You lost!, the PC used {pcWeponChoice} ")

def game():
    if(pcWeponChoice == myWeponChoice) :
        print(f"You both drew {pcWeponChoice}!!")
    elif(pcWeponChoice == "Rock"):
        if(myWeponChoice == "Paper"):
            won()
        if(myWeponChoice == "Scissor"):
            lost()
    elif(pcWeponChoice == "Paper"):
        if(myWeponChoice == "Scissor"):
            won()
        if(myWeponChoice == "Rock"):
            lost()
    elif(pcWeponChoice == "Scissor"):

        if(myWeponChoice == "Rock"):
            won()
        if(myWeponChoice == "Paper"):
            lost()  
    if(myWeponChoice != "Rock" or "Paper" or "Scissor"):
        print("You wrote something wrong bruh")
game()

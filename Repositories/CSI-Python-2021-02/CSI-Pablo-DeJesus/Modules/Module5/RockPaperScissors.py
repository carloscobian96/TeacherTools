


import random


foo = ['Rock', 'Paper', 'Scissors']
computerChoice = random.choice(foo)

UserChoice=input("Choose between Rock, Paper and Scissors ")


print(f"User picked {UserChoice}")
print(f"Computer picked {computerChoice}")
if(UserChoice=="Rock" and computerChoice=="Paper"):
  print("youlose")
elif(UserChoice==computerChoice):
  print(f"The computer picked {computerChoice}")



elif(UserChoice=="Rock" and computerChoice=="Scissors"):
     print("you win")


elif(UserChoice=="Rock" and computerChoice=="Rock"):
     print("tie")


elif(UserChoice=="Paper" and computerChoice=="Paper"):
     print("tie")


elif(UserChoice=="Paper" and computerChoice=="Scissors"):
     print("you lose")


elif(UserChoice=="Scisors" and computerChoice=="Scissors"):
     print("you lose")



else:
  print("enter valid value")
def greetStudent(name):
  print(f"Hello {name}!")

greetStudent("Carlos Quiñones")

var:str = "regular string"
myNumber:float = 3.5

myFunctionalString = f"Combine an existing {var} with a number such as: {myNumber} or execute something like {round(3.4 * 1.1)}"

print(myFunctionalString)

print(f"Or use the print directly {myNumber}")

def mealAsk():
    meal = input("What did you have for Breakfast?")
    print(meal)
    meal = input("what was your Lunch?")
    print(meal)
    meal = input("Have you had dinner?")
    print(meal)
mealAsk()
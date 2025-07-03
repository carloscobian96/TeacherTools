from datetime import datetime
from pathlib import Path

exec(open(Path(__file__).parents[2].joinpath("images/Logo.py")).read())

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

name = input("Hello there! What is your name? ")
studentId = input("What is your student id? ")

if name == "Carlos Quiñones":
  print("Hello me!!")
else:
  print(f" Your name is: {name} ")


print(f"Your Student id is: {studentId} ")
print(f"Currently, the time is: {current_time} ")

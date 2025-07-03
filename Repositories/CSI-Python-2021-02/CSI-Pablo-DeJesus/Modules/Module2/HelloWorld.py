from datetime import datetime
import os.path as path
from pathlib import Path 

myPath = str(path.join)(Path(__file__).parents[2],"images/logo.py"))
print(myPath)
with open(myPath, "r") as file: 
    exec(file.read())




now = datetime.now()
current_time = now.strftime("%H:%M:%S")

name = input("Hello there! What is your name? ")
studentId = input("What is your student id? ")

print(f"Hello {name}! ")
print(f"Your Student id is: {studentId} ")
print(f"Currently, the time is: {current_time} ")


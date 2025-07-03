#force.py

# Calculate force

def force (mass:float, acceleration:float): 
    return (mass * acceleration)

# values to two decimal places and use scientific notation

def printForce(force:float, unit: str):
    print(f"the force in scientific notation is: {force: .2e} {unit}.")

# Add a header to your execution. It includes 2 newline characters'\n'

printForce(force(4,8.3),"N")
printForce(force(2,9.9),"N")
printForce(force(3.4,7),"N")
printForce(force(5.7,6.2),"N")
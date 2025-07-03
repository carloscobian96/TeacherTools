# Areaofatriangle.py

# Calculate the area of a triangle

def areaOfATriangle(base:float, height:float):
    return (0.5 * base * height)

# Values to 2 decimal places and using scientific notation

def printAreaOfATriangle(areaOfATriangle:float, unit:str):
    print(f"The area in scientific notation is: {areaOfATriangle: .2e} {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'

printAreaOfATriangle(areaOfATriangle(30, 80), "m^2")
printAreaOfATriangle(areaOfATriangle(5, 10), "in^2")
printAreaOfATriangle(areaOfATriangle(100,300), "cm^2")
printAreaOfATriangle(areaOfATriangle(20,90), "mm^2")
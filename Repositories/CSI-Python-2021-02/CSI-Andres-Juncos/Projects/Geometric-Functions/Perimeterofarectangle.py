# perimeterofarectangle.py

# Here it's defining the equation for finding the perimeter
def perimeter(length:float, width:float):
        return ( (2 * length) + (2 * width) )

# Here its formating a value up to 2 decimal places, and printing a verbal representation with the unit.
def printperimeterScientific(perimeter:float, unit:str):
        print(f"The perimeter in scientific notation is: {perimeter:.2e} {unit}.")

# Here it's printing a header for the execution
print("\nCalculating various perimeters: \n")

# The execution itself
printperimeterScientific(perimeter(30, 10.7), "feet")
printperimeterScientific(perimeter(20.3, 8), "meters")
printperimeterScientific(perimeter(70.68, 50.47), "centimeters")
printperimeterScientific(perimeter(150.5, 20.2), "kilometers")

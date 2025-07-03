# perimeterofarectangle.py

# Calculate perimeter of a rectangle by using P= 2(length)+ 2(width)
def perimeter(length:float, width:float):
    return (2*(length)+2*(width))

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.

def printperimeterScientific(perimeter:float, unit:str):
    print(f"The perimeter in scientific notation is: {perimeter:.2e} {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating various perimeters: \n")

printperimeterScientific(perimeter(10, 50.5), "m^2")
printperimeterScientific(perimeter(53.3, 12.1), "m^2")
printperimeterScientific(perimeter(155.6, 150.7), "m^2")
printperimeterScientific(perimeter(125, 110.2), "m^2")

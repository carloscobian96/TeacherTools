# Perimeterofarectangle.py

# Calculate perimeter by using the length and width

def perimeter(length:float, width:float):
        return ( 2(length) + 2(width))

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.

def printPerimeterScientific(perimeter:float, unit:str):
        print(f"The perimeter in scientific notation is: {perimeter:.2e} {unit}.")

# Format a value to 2 decimal places. 
# Print a verbal representation with units.

def printPerimeterSimple(perimeter:float, unit:str):
        print(f"The perimeter is { round(perimeter, 2) } {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating various perimeters: \n")

printPerimeterScientific(perimeter(57, 32.0), "km")
printPerimeterScientific(perimeter(81.5, 7), "cm")
printPerimeterScientific(perimeter(9.46E2, 720), "ft")
printPerimeterScientific(perimeter(4.20E-6, 0.069), "yd")

# I am adding a space in between each example to separate them.
print()

printPerimeterSimple(perimeter(57, 32.0), "km")
printPerimeterSimple(perimeter(81.5, 7), "cm")
printPerimeterSimple(perimeter(9.46E2, 720), "ft")
printPerimeterSimple(perimeter(4.20E-6, 0.069), "yd")

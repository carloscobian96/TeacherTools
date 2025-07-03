# Area-of-a-Trapezoid.py

# Calculate the area of a trapezoid by using sides a and b divided by 2 times height.

def trapezoidArea(sideA: float, sideB: float, height: float):
    return (((sideA + sideB) / 2) * height)

# Format a value using 2 decimal places.
# Print a verbal representation with units.

def printTrapezoidArea(trapezoidArea: float, unit: str):
    print(f"The area of a trapezoid is: {trapezoidArea} {unit}.")

# Format a value to 2 decimal places. 
# Print a verbal representation with units.

def printTrapezoidAreaSimple(trapezoidArea: float, unit: str):
    print(f"The area of a trapezoid is { round(trapezoidArea, 2) } {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating the area of various trapezoids: \n")

printTrapezoidArea(trapezoidArea(2, 3, 5), "m^2")
printTrapezoidArea(trapezoidArea(4, 2, 6), "m^2")
printTrapezoidArea(trapezoidArea(87, 93, 5), "m^2")
printTrapezoidArea(trapezoidArea(23, 32, 2), "m^2")

# I am adding a space in between each example to separate them.
print()

printTrapezoidAreaSimple(trapezoidArea(7, 8, 9), "m^2")
printTrapezoidAreaSimple(trapezoidArea(4, 2, 0), "m^2")
printTrapezoidAreaSimple(trapezoidArea(13, 12, 6), "m^2")
printTrapezoidAreaSimple(trapezoidArea(67, 2, 13), "m^2")
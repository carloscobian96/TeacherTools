# Trapezoid.py

# Calculate the area of the trapezoid by dividing the sum of both its bases in half, and then multiply the result with the trapezoid's height.
def trapezoid (Base:float, base: float, Height: float):
        return ((Base + base / 2)*Height)

# Format a value using 2 decimals and scientific notation.
# Print a verbal representation with 2 units.
def PrintAreaScientific(trapezoid:float, unit:str):
        print(f"The area of the trapezoid in a scientific notation is: {trapezoid: .2e} {unit}.")

# Format a value to 2 decimal places.
# Print a verbal representation with the according units.
def PrintAreaSimple (trapezoid: float, unit: float):
        print(f"The speed is { round(trapezoid, 2)} {unit}.")

# Add a header to your execution that includes 2 newline characters '\n'.
print ("\nCalculating the area to various of trapezoids: \n")

PrintAreaScientific(trapezoid (78, 53, 19), "m^2")
PrintAreaScientific(trapezoid (31, 35, 58), "m^2")
PrintAreaScientific(trapezoid (25, 44, 86), "m^2")
PrintAreaScientific(trapezoid (123, 456, 789), "m^2")

# Add a space in between each example to separate them
print()

PrintAreaSimple(trapezoid (78, 53, 19), "m^2")
PrintAreaSimple(trapezoid (31, 35, 58), "m^2")
PrintAreaSimple(trapezoid (25, 44, 86), "m^2")
PrintAreaSimple(trapezoid (123, 456, 789), "m^2")
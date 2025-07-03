# AreaOfTriangle.py

# Calculate Area of Triangle by using the distance 
def area(base:float, height:float):
        return ( base * height * .5)

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.
def printAreaScientific(area:float, unit:str):
        print(f"The area in scientific notation is: {area:.2e} {unit}.")

# Format a value to 2 decimal places. 
# Print a verbal representation with units.
def printAreaSimple(area:float, unit:str):
        print(f"The area is { round(area, 1) } {unit}.")

# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating multiple areas: \n")

printAreaScientific(area(5, 68),"m^2")
printAreaScientific(area(55.5, 1),"m^2")
printAreaScientific(area(1.27E4, 290),"m^2")
printAreaScientific(area(1.27E-8, 0.001),"m^2")

# I am adding a space in between each example to separate them.
print()

printAreaSimple(area(10, 2.0), "m^2")
printAreaSimple(area(55.5, 1), "m^2")
printAreaSimple(area(2,23), "m^2")
printAreaSimple(area(1.27E-8, 0.001),"m^2")

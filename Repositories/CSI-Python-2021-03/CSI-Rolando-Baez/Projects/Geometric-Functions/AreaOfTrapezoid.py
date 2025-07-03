# Area of a Trapezoid
# defining the values and calculating the resut
def areaTrapezoid(a:float, b:float, height:float):
    return((a + b)/2 * height)

# By defining the area and units it allows us to the be able to print the result along with the unit
# In scientific notation
def printAreaTrapezoidScientific(areaTrapezoid:float, unit:str):
    print(f"The area of a trapezoid in scientific notation is: {areaTrapezoid: .2e} {unit}.")
# By defining the area and units it allows us to the be able to print the result along with the unit
# In simple form
def printAreaTrapezoidSimple(areaTrapezoid:float, unit:str):
    print(f"The area of a trapezoid is: {areaTrapezoid} {unit}")

print("\nCalculating area of Trapezoids: \n")
# Gives a header
#Prints our scientific notations
printAreaTrapezoidScientific(areaTrapezoid(100, 60, 50), "cm")
printAreaTrapezoidScientific(areaTrapezoid(4, 2, 5), "ft")
# Adds space between examples
print()
# Adds space between examples
#Prints in simple form
printAreaTrapezoidSimple(areaTrapezoid(2, 3, 5), "cm")
printAreaTrapezoidSimple(areaTrapezoid(150, 200, 300), "ft")



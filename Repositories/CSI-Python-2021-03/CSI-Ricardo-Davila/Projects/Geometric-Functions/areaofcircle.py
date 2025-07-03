#areaofcircle.py
import math

#Calculate area of a circle by using radius.
def areaofcircle(radius:float):
    return(radius*radius * math.pi)



#Format a value using 2 decimal places and scientific notation.
#Print a verbal representation with units.
def printAreaOfCircle(areaofcircle:float, unit:str):
    print(f"The area of the circle in scientific notation is: {areaofcircle: .2e} {unit}.\n")

#Add a header to your execution. it includes 2 newline characters '\n'
print("\nCalculating the area of different circles: \n")

printAreaOfCircle(areaofcircle(float(3)), "m²")
printAreaOfCircle(areaofcircle(25.3), "cm²")
printAreaOfCircle(areaofcircle(123.45), "mm²")
printAreaOfCircle(areaofcircle(5.2), "m²")


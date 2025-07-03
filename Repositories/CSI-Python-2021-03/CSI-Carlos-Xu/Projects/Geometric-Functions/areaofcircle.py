# areaofcircle.py
import math

#Calculate area of a circle by using radius multiplied by itself.
def areaofcircle(radius:float):
    return(math.pi  * radius*radius)


# Format a value using 2 decimal places and scientific notation
# Print a verbal representation with units

def printAreaofCircle(area:float, unit:str):
    print(f"The area of the circle using scientific notation is: {area: .2e} {unit} \n")


# Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating the area of different circles: \n")


printAreaofCircle(areaofcircle(3), "cm^2")
printAreaofCircle(areaofcircle(7.4), "ft^2")
printAreaofCircle(areaofcircle(4.9837), "m^2")
printAreaofCircle(areaofcircle(2.144E5), "mm^2")
printAreaofCircle(areaofcircle(988.1E-3), "cm^2")




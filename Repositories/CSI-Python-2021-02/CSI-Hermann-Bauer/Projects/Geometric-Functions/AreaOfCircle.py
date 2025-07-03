#import pi from math library
from math import pi
#function will take radius and unit. Will use formula pi times radius squared to return area in scientific notation
def areaOfCircle(radius:float):
    return (pi*radius*radius)

#Will call areaOfCircle and print the area with the units
def printAreaOfCircle(radius, unit):
    print(f"The area of the circle is {radius:2e} {unit}")

#take the radius
radio = input("Input radius: ")
#take the units
unit = input("Unit: ")

#will call areaOfCircle and printAreaOfCircle and units
printAreaOfCircle(areaOfCircle(radio), unit)
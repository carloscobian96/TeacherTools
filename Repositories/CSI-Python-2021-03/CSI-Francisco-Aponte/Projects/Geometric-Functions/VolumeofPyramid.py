# VolumeOfPyramid.py

# I defined the varibles in the formula for the volume of a pyramid
def VolumeOfPyramid(a:float, b:float):
                return ( a * b / 3)

# I definied the the function VolumeOfPyramidSN which calls the function from the code before, and turns it into Scientific Notation
def printVolumeOfPyramidSN(VolumeOfPyramid:float, unit:str):
    print(f'The volume of the pyramid in scientific notation is: {VolumeOfPyramid:.2e} {unit}')

# I added a title to the rsults of the equation
print("\n Calculation the volume of various pyramids\n")

# Here, the code says what a and b are, and calculates using the formula it was given. Then it adds the unit at the end (cm^3)
printVolumeOfPyramidSN(VolumeOfPyramid(15, 25), "cm^3")
printVolumeOfPyramidSN(VolumeOfPyramid(99, 26), "cm^3")
printVolumeOfPyramidSN(VolumeOfPyramid(35, 22), "cm^3")
printVolumeOfPyramidSN(VolumeOfPyramid(44, 121), "cm^3")
# 
#
import math
# VolumeofSphere

#Calculate the volume of a sphere using the radius

def VoS(radius):

    return((4/3)*(math.pi)*(radius)*(radius)*(radius))
#This function prints the result given by the Vos function in scientific notation and with the proper units
def printScientificNote(VoS:float,unit:str):
    print(f"The Volume of a Sphere in scientific notation is:{VoS:.2e}{unit}")
#This line prints a header for the projects
print("\nCalculating various Volumes of spheres: \n")
#THe printScientificNote function is called with the result of VoS as a parameter
printScientificNote(VoS(4.36),"cm^3")
printScientificNote(VoS(8.39),"cm^3")
printScientificNote(VoS(10.23),"cm^3")
printScientificNote(VoS(39.8),"cm^3")
# This function is used for the formula used for calculating the volume of a rectangular prism
def volume(length:float, width:float, height:float):
        return ( length * width * height)


# This function calls the function volume and calls it. It puts the volume of the rectangular in scientific notation.
def printVolumeScientific(volume:float, unit:str):
        print(f"The volume of the rectangle prism in scientific notation is: {volume:.2e} {unit}.")

# This part is where the program prints the volumes in scientific notation.
print("\nCalculating various volumes: \n")

printVolumeScientific(volume(9.8, 24.5, 67.3), "m^3")
printVolumeScientific(volume(13.8, 28.3, 40.6), "m^3")
printVolumeScientific(volume(18.9, 35.2, 80.4), "m^3")
printVolumeScientific(volume(21.7, 31.4, 90.3), "m^3")

#volumeofarectangularprism.py

# Calculate the volume by multiplying length times width times height
def volume(length:float, width:float, height:float):
    return ( length * width * height)

# Format a value using 2 decimal places and scientific notation. 
# Print a verbal representation with units.
def printVolumeScientific(volume:float, unit:str):
    print(f"volume in scientific notation is: {volume: .2e} {unit}.")

    # Add a header to your execution. It includes 2 newline characters '\n'
print("\nCalculating various volumes: \n")

printVolumeScientific(volume(200, 55.0, 73.15), "cm^3")
printVolumeScientific(volume(65.0, 2, 13), "mm")
printVolumeScientific(volume(3.27E4, 190, 56), "ml")
printVolumeScientific(volume(1.47E-8, 0.01, 34), "mm^2")



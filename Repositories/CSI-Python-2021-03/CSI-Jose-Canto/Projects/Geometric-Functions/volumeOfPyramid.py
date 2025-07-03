# volumeofpyramid.py

# Calculate the volume of a pyramid using the Volume = Base x Height x width divided by 3
def volume(base:float, width:float, height:float):
    return ((base * width * height)/3)

# This will format the value using 2 decimal places and scientific notation.
# Print the verbal representation with units

def printVolumeScientific(volume:float, unit:str):
    print(f"The volume in sceintific notation is {volume:.2e} {unit}.")

# Add header to your execution. It includes 2 newline characters '\n'

print("\nCalculating various volumes: \n")

printVolumeScientific(volume(22.2, 5, 8), "mL")
printVolumeScientific(volume(55.5, 1E2, 4E2), "mL")
printVolumeScientific(volume(2.37, 29.0, 40.3), "mL")
printVolumeScientific(volume(1, 0.001, 0.302), "mL")
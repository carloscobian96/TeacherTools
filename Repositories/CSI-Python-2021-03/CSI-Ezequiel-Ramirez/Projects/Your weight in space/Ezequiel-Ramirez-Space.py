Planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print("Calculate your weight in a different planet of our Solar System!")

MyWeight = int(input("What is your weight in pounds? "))

PlanetString = str(Planets).replace("\'","").replace("[","").replace("]","")
MyPlanet = input(f"Select a planet from the list: {PlanetString} ")

def CalculationWeight(Planet:str,mass):
    print(f"Earth mass in pounds is: {mass}")

    w_kg = mass / 2.2046
    print(f"Mass in kg: {w_kg}")

    n_lb = 4.45

    Planet = Planets.index(Planet)

    print(f"Weight in {Planets[Planet]} is {(round(w_kg * g_ms2[Planet]) / n_lb)} lb. \n")

CalculationWeight(MyPlanet,MyWeight)
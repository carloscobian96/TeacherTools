planets = [["Mercury", 3.7],["Venus", 8.87],[ "Earth", 9.81],["Mars", 3.711],["Jupiter", 24.79],[ "Saturn", 10.44], ["Uranus", 8.69], ["Neptune",11.15]]

print(f"{planets[0][0]},{planets[1][0]},{planets[2][0]},{planets[3][0]},{planets[4][0]},{planets[5][0]},{planets[6][0]},{planets[7][0]}")
#Aqui puedo usar un pipe enves d formating: string(planets.replace("\,"))
userLocation = input("So, in which of these planet you at?")

userMass = float(input("What's your mass in kilograms?"))


for planet in planets:
    if(planet[0] == userLocation):
      userGravity = planet[1] 
      userWeigth  =round(userGravity * userMass* 0.0224808943 )
      print(f"Your weigth in {userLocation} is {userWeigth}lbs")





    
    
    

# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
def send(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def checkInput():
    while True:
        num = input("Enter a number between 0 and 9 to be displayed: ") # Asks the user for a number
        numInt = int(num)
        if(numInt > 9 or numInt <0 ):
            print("The number has to be beween 0 and 9")
            
            continue
        else:
            break
    return num
            
    


while True:
    num = checkInput()
    value = send(num)
    
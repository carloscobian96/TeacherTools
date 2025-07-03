import random

#La variable steps contiene las diferentes etapas del hangman
steps = ["""             
          |----------|
          |
          |
          |
          |
          |
          |
          |
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |        
          |
          |
          |
          |
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |          |
          |          |
          |
          |
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|
          |          |
          |          
          |         
         """,   
        
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|---
          |          |
          |
          |
         """,
            """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|---
          |          |
          |          ^
          |         ^
         """,
         """            
          |----------|
          |         OO
          |        ---- 
          |          | 
          |       ---|---
          |          |
          |          ^
          |         ^ ^
         """]

#La lista de used_letters se utiliza para poner en una lista las letras de la palabra que hay que adivinar para que una vez adivine la primera letra, verifique si está en esta lista y puede seguir corriendo el código
# used_letters =[]
#La lista de invalid_caracters contiene todos los simbolos que no se pueden utilizar en la palabra para que una vez adivine la primera letra, verifique si está en esta lista y puede seguir corriendo el código
invalid_caracters= ["!","@","~","`","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|",":",";","'","<",",",".",">","/","?"]
#La lista de invalid_numbers
invalid_numbers = ["0","1","2","3","4","5","6","7","8","9"]
# Lista de palabras
word_list = ["playa","oceano","patineta","zapato","tabla","generador","palma","computadora","televisor","pelicula","fotografia","comida","Patillas","Barceloneta","municipio","Vieques","gobernador","ventana","Aibonito","Culebra"]
# variable con underscore para que esto se utilize en una función más adelante.
wrong_letter = "_"

# esta funcion escoge una palabra al azar de la lista word_list para que esta palabra sea la que la persona tiene que adivinar
def get_word():
    word =  random.choice(word_list)
    return word.upper()
# esta variable pone el resultado de la funcion anterior en ua variable para así utilizarla en otras funciones y lógicas más adelante.
my_word = get_word()

# esta funcion establece las limitaciones que tiene la letra adivinida utilizando lógicas
def get_input():
    
    while(True):
        letter = input("Chose your letter").upper()
        # esta lógica estabece que la letra adivinada tiene que ser de 1 caracter, no puede tener más de 1 ni menos de 1
        if(len(letter)!= 1):
            print("error")
            continue
        # esta lógica establece que si la letra adivinada es repetida, te dirá que ya la utilizastes 
        if(letter in used_letters):
            print("You already used this letter")
            continue
        # esta lógica establece que si la letra adivinadaes un número, se imprimirá un error
        if(letter in invalid_numbers):
            print("error")
            continue
        # esta lógica establece que si la letra es un síbolo y no una letra, se imprimirá un error
        if(letter in invalid_caracters):
            print("error")
            continue
        
        used_letters.append(letter)
        return letter

# esta función te imprime la palabra según la vayas adivinando. Si la letra que adivinaste está bien, se imprime la letra seleccionada en los lugares que corresponde, si está incorrecta, se imprimirán underscores en los lugares que no hayas adivinado.
def print_word():
    #  temp es una variable vacía que se irá contruyendo según la lógica de esta función
    temp:str = ""
    # len(word)
    for letter in my_word:
        # esta lógica dice que si la letra adivinada está bien, se primirá en los lugares que esté
        if (letter in used_letters):
            temp = temp + letter
        # esta lógica dice que si la letra adivinada está mal, se imprimirán underscores
        else:
            temp = temp + "_"
        
    # esto imprimirá el temp o la palabra creada después de cada adivinación
    print(temp)
    return temp

# esta función está encargada de imprimir cada paso del hangman según vayas adivinando
    
def print_steps(): 
    # counter es una variable con el valor 0 que se utilizará para imprimir los pasos
    counter= 0
    for letter in used_letters:
        # si la letra adivinada está incorrecta, se imprimirá el paso siguiente, eso es lo que significa el counter +1
        if letter not in my_word:
            counter= counter + 1
    # esto imprime el paso que calculó la función
    print(steps[counter])  
    
    return counter


#aquí, estoy diciendo que escoga una palabra nueva para continuar con otro juego
while True:
    my_word = get_word()
    used_letters = []

# Aquí, es que se reinicia el juego
    while True:
        counter = print_steps()
        get_input()
        myTempString = print_word()
        
        # si esta mal la palabra, se imprime lo siguiente y se reiniciará
        if(counter == 6):
            print(f"You lose! The correct word was {my_word}. Play Again.")
            break
       # imprime las letras utilizadas anteriormente
        used_letters_list = str(used_letters).replace('\'','').replace('[','').replace(']','')
        print(f"These are the letters you have used: {used_letters_list} ")

        # si esta bien la palabra, se imprime lo siguiente y se reiniciará
        if(myTempString == my_word):
            print("You Won!! Play Again.")
            break


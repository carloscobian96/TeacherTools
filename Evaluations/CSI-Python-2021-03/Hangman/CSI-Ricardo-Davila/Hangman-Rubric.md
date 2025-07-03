# Hangman Rubric: CSI-Ricardo-Davila

## Score: /100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| Instructions              | 30 |  | 
| random word               | 5  |  | 
| multiline string array    | 5  |  | 
| Validate input            | 15 |  | 
| Find matches              | 10 |  | 
| Display the current step  | 10 |  | 
| Display attempted letters | 10 |  | 
| game progression          | 10 |  | 
| restart game              | 5  |  | 

<br>

### Submitted Work: 

```python


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


```




# Instructions:

<div style="text-align:center">
        <img    src="https://media.istockphoto.com/illustrations/simple-illustration-of-hangman-game-illustration-id1196954772?k=20&m=1196954772&s=612x612&w=0&h=nzsr9bCwxp9xW3dp-nBJeXE7TVGqnWtdJpbaXvEyl3E="
                width="50%" 
                height="50%" />          
</div>

<br>

# Hangman `100pts Total`

<br>

### Instructions: `(30pts)`
* Create `Hangman.py` in this folder.
* Define a function for each objective.
* Document every line of the code.


<br>

## Select a random word. `(5pts)`
You may select a random word by one of 2 ways:
1. Create a list with at least 20 words and use `random()`
2. Fetch a random Word from an API. This may be done by using the *HTTP Request deserialization* code used in `Web-Servers`.

Print out it's length represented by underscores:

eg. MAGISTERIO
``` 
_ _ _ _ _ _ _ _ _ _
```

<br>

## Create a multiline string array for each step of the game. `(5pts)`
```python
steps = [
        """
        1
        """,
        """
        2
        """]
```

<br>

## Validate input `(10pts)`
Accept a single character from the user as input. You must ensure to receive a valid character.
* A single character long
* Not a number
* Not a symbol
* User has not attempted the letter already.
  * Create a list to store attempted characters
* Must handle lower case and upper case letters.

<br>

## Find matches in your word. `(10pts)`
Print out underscores combined with successfully matched characters.
``` 
M _ G _ S _ E _ I _
```

<br>

## Display the current step of the game by addressing it's index of the array. `(10pts)`
You must develop a mechanism to keep track of which step you're on base of failed attempts.
```python
# Example of printing the fist step in hangman.
print(steps[0])
```

<br>

## To-Do:
1. Display attempted letters List. `(10pts)`
2. Logic for game progression.`(10pts)`
3. Loop to restart game. `(5pts)`
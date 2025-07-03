
from multiprocessing.connection import wait
import random 
import urllib.request
import json
from xml.sax import parseString
from RandomHipsterStuff import RandomHipsterStuff#import el class 

import sys 



def delDuplicate(hipAr):#this function deletes words that have duplicated letters
    for word in hipAr:
        string =word
        #print(string)
        #Counts each character present in the string  
        for i in range(0, len(string)):  
            count = 1;  
            
            for j in range(i+1, len(string)):  
                if(string[i] == string[j] and string[i] != ' '):  
                    count = count + 1;  
                    #Set string[j] to 0 to avoid printing visited character  
                    string = string[:j] + '0' + string[j+1:];  
                # print(string)
                # print(f"{string}:{duplicates}")
            
            #A character is considered as duplicate if count is greater than 1  
            if(count > 1 and string[i] != '0'):  
                duplicates.append(string[i])
            else :
                zero.append(string)

    notZero =[]
    for f in zero:
        if("0" not in f):
        
            notZero.append(f)

    for rep in notZero:
      #  print(f"{len(rep)} : {rep}")
        #print(f"{notZero.count(rep)} : {rep}")
        
        if(len(rep)== notZero.count(rep)): 
            #print(rep)
            global hipWord
            hipWord = rep
            hipWord =hipWord.lower()
            single = True
            break
    


    #hipWord = hipAr[0]

            
   # print(notZero)           
   # print(hipAr) 
   # print(hipWord)
    #if a word without duplicates was not found return False
    if(single != True):
        return False
    if(single==True):
        return single
    #print(duplicates)



def getHips():#Esta funcion busca los hipWords

    hipUrl = "https://random-data-api.com/api/hipster/random_hipster_stuff?"
    #URL used too get the 

    req = urllib.request.Request(hipUrl)
    requestData = json.loads(urllib.request.urlopen(req).read())

    myHipster = RandomHipsterStuff(**requestData)

    #hipAr is an array made of 3 hipster words
    hipAr = myHipster.words
    duplicated = delDuplicate(hipAr)

    while duplicated== False:
        getHips()
       # print("no")
        #If no word without a duplicate was found call the function again
        
    return hipWord

count = 0
#Here i define the variables I will use later
duplicates = []
duplicateDict={}
duplicateIndex=[]
zero = []
try:
    hipWord= getHips()
except:
    
   sys.exit()
hipLetters = ""

#print(hipAr)


hipLetters = list(hipWord)
#THe word is turned into a list to iterate later
guessedWrong= []
correctIndex=[]

hangedImgAr= [""" 
     _____________
     |/      |
     |      
     |
    _|___
   """,""" 
     _____________
     |/      |
     |      (_)
     |      
     |
    _|___
   """,
   """ 
     _____________
     |/      |
     |      (_)
     |       |
     |       
     |
    _|___
   """,""" 
     _____________
     |/      |
     |      (_)
     |      \|
     |
    _|___
   """,
   """ 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       
     |
    _|___
   """,""" 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
   """,
   """ 
     _____________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
   """]

guessedWords= []
correctWords=[]
finished = False
def getInput() :#esta funcion filtra return el guess
    while(True):
     
        guess=input("What is your guess?")
       
        if guess.isnumeric()== True :
            print("Cant be a number")
            #if guess is a number
            continue

        if len(guess)!=1 :
            print("Must only be one letter")
            #if guess uses more than one letter
            continue
        if not guess.isalpha():
            print("Can't include special characters")
            #if guess is special char
            continue
        if(guess in guessedWords):
            print("Bruh you already guessed it fracaso")
            continue
        return guess

def Ronda(hipWord):#Esta es la funcion repetida cada Ronda ovcio 
     
     lengthOfWord = len(hipWord)
     #get the length of the word
        
  
     answeLine = ""
     

     for letra in correctWords:
         hipWord.index(letra)
         #get the location of the word guessed in the word that is meant to be guessed
         correctIndex.append(hipWord.index(letra))
         #append all of the  lines should be filled to a list
        # print(correctIndex)
        
     for x in range(lengthOfWord):

        if(x in correctIndex):
         answeLine = answeLine + f"_{list(hipWord)[x]}__   "
         #if the index of the letter guessed is the iteration of the line then print the letter on the line
         #es dificil de explicar sorry
        else:
         answeLine = answeLine + "___   "
        #si no es lo otro pues bregemos
    
     try:
        print(hangedImgAr[len(guessedWrong)])
        #Si el numero de fallos exede 5 pues se acabo el juego
     except:
         #print("YOU LOST")
         print("""
                      _
         (_) -
               '
       @_  _    '
        )\/(@    '
      __(/ \--._
     (,-.---'--'@
      @ )0_0(     _
        ('-')    (_)
   '    _\Y/_      
   ' .-'-\-/-'-._  '
   _ /    '*     \ '
  (_)  /)  *    .-.))>'
    ._/  \__*_ /\__'.
'<((_'    |___/  \__\\
          /   ,_/ |_|
          )-- /   |x|
          \ _/    (_ x
          /_/       \_\@
         /_/
        /_/
       /x/
      (_ x
        \_\@
     QUE PAYASO LOL           
                 """)
         print(f"JAJAJ, the word was {hipWord}")

         playAgain = input("Wanna loose again, i mean play again?!?!?")
         if(playAgain == "yes" or playAgain == "ok" or playAgain == "sure" or playAgain == "affirmative" or playAgain == "okay" or playAgain == "yea" or playAgain == "all right" or playAgain == "by all means" or playAgain == "gladly" or playAgain == "yep" or playAgain == "very well"):
            StartGame(hipWord)

     print(f"Im thinking of a super cool rad {lengthOfWord} letter word")
     print(f"Guessed Wrong: {guessedWrong}")
     print(answeLine)
     #this print is repeted every round
    # print(hipWord)    
     guess = getInput()
     #self explanitory
   
    # print(hipLetters)
     for letter in hipLetters:
                
                if(guess == letter ):
                    #is guess is a letter in the word pues bien por ti
                    correct = True
                   
                   
                    
                    
                    break
                else:
                   #si no pues False
                   correct = False

                   
    
     guessedWords.append(guess)
     #Todas las palabras adivinadas correctas o no van a esta lista
     if(correct):
            print("You guessed rigth")
            correctWords.append(guess)
         
     else:
            print("You guessed wrong")
            guessedWrong.append(guess)
               #self explanotory

 
     count = 0       
     
     
     
     if len(hipWord)==len(correctWords) :
         finished = True
         #si el numero de  las letras correctas es igual al numero de letras en el hipWord GANASTE
     else :
         finished = False

def StartGame(hipWord):#Este es el Main FUnction
    print("""
   __________________                         __________________
| _    _______    /  /                       | _    _______    /  /
|(_) .d########b. //)| _____________________ |(_) .d########b. //)|
|  .d############//  ||        _____        ||  .d############//  |
| .d######""####//b. ||()||  [CARLOSQ]   |()|| .d######""####//b. |
| 9######(  )#_//##P ||()|__|  | = |  |__|()|| 9######(  )#_//##P |
| 'b######++#/_/##d' ||() ||   | = |   || ()|| 'b######++#/_/##d' |
|  "9############P"  ||   ||   |___|   ||   ||  "9############P"  |
|  _"9a#######aP"    ||  _   _____..__   _  ||  _"9a#######aP"    |
| |_|  `######''     || (_) |_____||__| (_) || |_|  `######''     |
|  ___..___________  ||_____________________||  ___..___________  |
| |___||___________| |                       | |___||___________| |
|____________________| COOL HIPSER BOOM BOX  |____________________|  
    """)
    welcome = input("Welcome to my super hipster hangman game?Wanna play?")
    #welcome statement
    if(welcome == "yes" or welcome == "ok" or welcome == "sure" or welcome == "affirmative" or welcome == "okay" or welcome == "yea" or welcome == "all right" or welcome == "by all means" or welcome == "gladly" or welcome == "yep" or welcome == "very well"):
        #si una palabra afirmativa se usa pues LETS START DA GAME
        print("lets get started!!")

        #hipWord = getHips()
        for j in range(0,100):
            #no actually va a repetirse 100 veces pq hay un sys.exit
            Ronda(hipWord)
            #empiesa la ronda!!!
            if len(hipWord)==len(correctWords) :
                 break
                #si brego pues exit el loop
            if(len(guessedWrong)== 6):
                print("YOU LOST!")
            
                #si perdiste la mala
            
            
             
        print("YOU WINNN!!!!!")
        playAgain = input("Wanna play again?")
        if(playAgain == "yes" or playAgain == "ok" or playAgain == "sure" or playAgain == "affirmative" or playAgain == "okay" or playAgain == "yea" or playAgain == "all right" or playAgain == "by all means" or playAgain == "gladly" or playAgain == "yep" or playAgain == "very well"):
            StartGame(hipWord)

        print("""
              @=====@
                #=@       @=#_
               # \/\/\/\/\/\ #\\
               @@|  _   _  |@@(
               @@|\|_|-|_|/|@@ )
                @|    /\   |@ (
                 |  \~~~~/ |   )
                 |   ~~~~  |   |
                  \_______/    |
           _________|   |_______(____
          /         \   /      (     `\\
         /  / |  fvk \ /      |-\---,  \\
 _______/  /__|_______@_______|__)___\  \________
|\      \  \___   ______________#     |  |__     \\
|\\\      /\ \  ', |\ # W W W W @@ \   /ooo  `,    \\
||\\\    '  ooo   \\#\ # W W W W @@ \ '        \    \\
|| \\\    \       ; \#\___o_o_o_o____\ \       ;     \\
\|_|\\\    `,_____/  \|______________|  `,_____/      \\
     \\\                                               \\
      \\\     LETS GOOOOOOOOOOOOOOOOOOOOOOOOO!!!        \\
       \\\_______________________________________________\\
        \  ___________________________________________  |
        || |                                         || |
        || |                                         || |
        || |                                         || |
        \|_|                                         \|_| 
       
        """)
          
    else:
        print("awww")



StartGame(hipWord)
#call el main funtion


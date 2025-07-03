import random

steps = ["""
 
      ___________
     [          []
     ]          []
                []
                []
                []
                []
                []
    ==============
""",
"""

      ___________
     [          []
     ]          []           
    / \         []
    \_/         []
                []
                []
                []
                []
    ==============

""",
"""
      ___________
     [          []
     ]          []           
    / \         []
    \_/         []
    | |         []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
    \_/ /       []
    | |/        []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
                []
                []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
      \         []
       \        []
    ==============

""",
"""

     ___________
     [          []
     ]          []           
    / \         []
  \ \_/ /       []
   \| |/        []
    |_|         []
    / \         []
   /   \        []
    ==============

"""
]
#This function chooses a random word from a list using random.choice and will then make that word the "Hangman Word" which is defined as hangmanWord
def get_word():
  possibleWords = ['ponce', 'guaynabo', 'fajardo', 'bayamon', 'carolina', 'cabo rojo', 'san juan', 'aguadilla', 'moca', 'lajas', 'arecibo', 'orocovis', 'cayey', 'corozal', 'salinas', 'arroyo', 'yabucoa', 'humacao', 'ceiba', 'luquillo']
  hangmanWord = random.choice(possibleWords)
  return hangmanWord

#This function is supposed to create a list titled "lettersList" in which letters will be put into once used for then to be used in other functions
def used_letters():
  lettersList = []
  maxTries = 15
  while len(lettersList) < maxTries:
    lettersList.append

#This function prints the blank spots of the word per letter
def print_word(hangmanWord):
  blank_word = len(hangmanWord) * '_'
  word = print(blank_word)
  return word

#This function will get the input and validate it using isalpha which will only use alphabetical characters
def get_input():
  while True:
    letter = input("Choose letter")
    if letter.isalpha():
      print("Choose a valid character (A letter from a to z)")
      continue
      
    return letter
 
 #This will check if the letter is found within the word or if it's not. If it's not the step will print giving the player one less chance to guess (if this worked correctly (it doesn't))
def word_check(letter, hangmanWord, lettersList):
      if letter not in hangmanWord:
        print('Incorrect guess...')
        lettersList.append(letter)
        print (steps[0])
        print(lettersList)
      if letter in hangmanWord:
        print('Correct Guess!')
        lettersList.append(letter)
        print(lettersList)

# After a letter is guessed, this function will check if that letter corresponds to a certain letter within the word and it will fill it in
def fill_blanks(letter, hangmanWord, lettersList):
  temp = ""
  for letter in hangmanWord:
    if(letter in lettersList):
      temp = temp + letter
    else:
      temp = temp + '_'

get_word()

print_word('hangmanWord')

get_input()

used_letters()

word_check()

fill_blanks()


    

hangmanWord = 'test'
while True:
   letter = input("Choose letter")
   if letter.isalpha():
     break
   print("Please Choose a valid Character")  

blank_word = len(hangmanWord) * '_ '
print(blank_word)
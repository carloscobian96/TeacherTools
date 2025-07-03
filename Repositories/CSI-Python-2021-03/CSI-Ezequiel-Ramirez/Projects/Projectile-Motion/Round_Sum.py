def Round_Sum(a, b, c):
#This is the function that contains the integers that will be rounded up.
      return Round10(a) + Round10(b) + Round10(c)
#The Round10 function, defined later, is applied here to all of the integers before adding them up.

    
def Round10(Num):
#This function is the one responsible for actually rounding the integers.
    if Num % 10 < 5:
        return Num - (Num % 10)
#This if statement is responsible for rounding up the integers that are 5 or more with a special equation.
        
    return Num + (10 - Num % 10)
#This return statement is responsible for rounding down the integers below 5.

print(Round_Sum(16, 17, 18))
print(Round_Sum(12, 13, 14))
print(Round_Sum(6, 4, 4))
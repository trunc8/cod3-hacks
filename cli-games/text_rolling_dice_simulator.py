#trunc8

"""random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)"""


import random

try:
    n = int(input("How many sided dice? "))
except ValueError:
   print("That's not a valid input!")
   exit

while True:
    print("Number on the dice: ", random.randint(1,n))
    choice = input("Do you wanna roll again(y/n)? ")
    if choice!='y':
        break


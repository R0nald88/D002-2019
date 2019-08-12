# D002 Lesson 3
# Q1:  Warm up exercise

# a) Go Dutch
from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin pay the bill first. But Kevin only has 100 dollar notes")
a=ceil(bill/100)
b=a*100-bill
c=bill*people/ (people+1)
print("So Kevin is going to pay $%d." % int(a))   # replace with your code
print("The cafe is giving %f to Kevin." % float(b))  # replace with your code
print("Each one should give %f to Kevin." % float(c)) # replace with your code

# b) Clap at Seven 
# The purpose of the following program is to print the number from 1 to 100,
# in order. However, when the number is a multiple of 7 (e.g. 7/14/21) or when
# the last digit of the number is 7 (e.g. 17/27/37), it print a X instead

number = 1
while number <= 100:
    if number % 7 == 0 or (number -7)% 10 ==0:   # replace with your code
        print('X', end=' ')
    else:
        print(number, end=' ')    
    number = number + 1
print("\nGame Over.")

# c) How long it takes?
# In a Chinese board game the player can start its game only when he can
# get a 6 in rolling a dice. Please do an experiment to test your luck today
# and see how long it takes to get a dice

from random import randint

#code for rolling a dice
number = randint(1,6)
count = 1
while number != 6 : # replace with your code
    # Write some more code
    number = randint(1,6)
    print("I got a %d" % number)
    count = count + 1

print("Oh, it takes me %d times to get a 6!!!" % count)


# d) How long it takes, in general?
# Repeat the experiment in part c for 100 times and see what is the average 
# value of the count would be. This is challenging, isn't it?

from random import randint

#code for rolling a dice
number = randint(1,6)
count = 1
n=1
while n <=100:
    number = randint(1,6)
    while number != 6 : # replace with your code
        # Write some more code
        number = randint(1,6)
        count = count + 1
    n+=1
print("Oh, it takes me %d times to get a 6 100 times!!!" % count)
print('The average probability is %f' % float(count /100))  













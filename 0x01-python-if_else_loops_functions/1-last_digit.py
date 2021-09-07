#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = 10 - number % 10
else:
    lastdigit = number % 10
if lastdigit == 0:
    theanswer = "and is zero"
elif lastdigit > 5:
    theanswer = "and is greater than 5"
else:
    theanswer = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, lastdigit, theanswer))

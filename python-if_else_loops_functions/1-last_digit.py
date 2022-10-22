#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(repr(number)[-1])
number1 = int(last)

if number < 0:
    if int(last) == 0:
        last == 0
    else:
         last = ("-" + last)


if int(last) > 5:
    number1 = " and is greater than 5"
if int(last) == 0:
    number1 = " and is 0"
if int(last) < 0:
    number1 = " and is less than 6 and not 0"


print("Last digit of "+ str(number) + " is " + last + number1)


"""import random
number = random.randint(-10000, 10000)

if number < 0:
    remainder = number % (-10)
else:
    remainder = number % 10

if remainder > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, remainder))
elif remainder is 0:
    print("Last digit of {} is {} and is 0"
          .format(number, remainder))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, remainder))"""

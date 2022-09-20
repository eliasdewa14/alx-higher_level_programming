#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1

if last_digit == 0:
    str = "0"
elif last_digit <= 5:
    str = "less than 6 and not 0"
else:
    str = "greater than 5"
print("Last digit of {} is {} and is {}".format(number, last_digit, str))

"""
A simple die roller

Author: Gabriel Martinez
Date: August 5, 2020
"""

import random

first = input('Type the first number: ')
first = int(first)

last = input('Type the last number: ')
last = int(last)

roll = random.randint(first, last)

print('Choosing a number between ' + str(first) + ' and ' + str(last) + '.')
print('The number is ' + str(roll) + '.')

"""
A simple die roller

Author: Gabriel Martinez
Date: August 5, 2020
"""

import random

first = 1

last = 6

roll = random.randint(first, last)

print('Choosing a number between ' + str(first) + ' and ' + str(last) + '.')
print('The number is ' + str(roll) + '.')

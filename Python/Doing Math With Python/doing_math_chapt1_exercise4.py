# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Fraction Calculator

"""
Fraction operations
"""

from fractions import Fraction


def add(a, b):
    print('Result of Addition: {0}'.format(a+b))


if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
    if op == 'Add':
        add(a,b)

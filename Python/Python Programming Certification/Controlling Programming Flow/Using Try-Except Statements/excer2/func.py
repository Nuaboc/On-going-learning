"""
A function to test for floats in European format

Author: Gabriel Martinez
Date: September 9, 2020
"""
import introcs


def iseurofloat(s):
    """
    Returns True if s is a float in European format.  Returns False otherwise.

    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See

        https://en.wikipedia.org/wiki/Decimal_separator

    for more information.

    This function does not recognize floats in scientific notation (e.g. '1e-2').

    Examples:
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False

    Parameter s: The string to check
    Precondition: s is a string
    """
    assert type(s) == str

    try:
        print('try')
        coma = introcs.index_str(s, ',')
        print('1')
        negative = '-' in s[coma + 1]
        print(2)
        error1 = introcs.index_str(str(negative), str(False))
        print(3)
        begin = ',' == s[0]
        print(4)
        error2 = introcs.index_str(str(begin), str(False))
        print(5)
        dot = '.' in s
        print(6)
        error3 = introcs.index_str(str(dot), str(False))
        double = ',' in s[coma + 1:]
        error4 = introcs.index_str(str(double), str(False))
        return True

    except:
        print('except')
        return False

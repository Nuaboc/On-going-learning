"""  
A function to check the validity of a numerical string

Author: Gabriel Martinez
Date: August 31, 2020
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    assert len(s) <= 7

    # check = introcs.
    num_string = bool
    check = test(s)

    if s[0] == '0' and len(s) > 1:
        num_string = False
        print(1)
    elif not check:
        num_string = False
        print(2)
    else:
        num_string = True
        print('last')

    # if it cant be concatenated it returns false.

    return num_string


def test(s):
    find = introcs.find_str(s, ',')
    if s[find] != s[-4] and len(s) > 4:
        # print(find)
        print('a')
        return False

    elif find != -1 and len(s) > 4:
        remove = introcs.replace_str(s, s[find], '')
        print('b')
        return introcs.isdecimal(remove)

    elif find == -1 and len(s) <= 3:
        print('c')
        return introcs.isdecimal(s)

    else:
        print('d')
        return False


print(valid_format('91,2345'))

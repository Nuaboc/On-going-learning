"""
Functions demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: Gabriel Martinez
Date: September 23, 2020
"""


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Examples:
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    c = s.find('(') + 1
    d = s.find(')', c)
    sub = s[c:d]

    return sub


def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.

    Cornell network ids consist of 2 or 3 lower-case initials followed by a
    sequence of digits.

    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False

    Parameter s: the string to check
    Precondition: s is a string
    """
    check1 = s[0:2].isalpha()
    check2 = s[0:2].islower()
    check3 = s[2:].isdigit()

    check4 = s[0:3].isalpha()
    check5 = s[0:3].islower()
    check6 = s[3:].isdigit()

    if check1 and check2 and check3:
        return True
    elif check4 and check5 and check6:
        return True
    else:
        return False

"""
The functions for the course project.

Author: Gabriel Martinez
Date: July 31, 2020
"""

import introcs


def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    assert introcs.find_str(s, '(') > 0 and introcs.find_str(s, ')') > 0, 'this sucks'
    first_open = introcs.find_str(s, '(')
    print(first_open)
    first_close = introcs.find_str(s, ')', first_open, -1)
    print(first_close)
    # Compare both searches to -1 and return True if BOTH are not -1
    result = first_open != -1 and first_close != -1 or s[first_close] == ')'
    return result


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str, "Value error! Use only string as argument."
    assert matching_parens(s)

    before = len(s[:introcs.find_str(s, '(')])
    after = len(s[:introcs.find_str(s[before + 1:], ')')])

    result = s[before + 1:after + before + 1]
    return result

'''
x = '123'
print(x.index('3'))
print(x[2])
print(x[-1])
'''
# print(matching_parens('(A B)'))
print(first_in_parens('))(()'))

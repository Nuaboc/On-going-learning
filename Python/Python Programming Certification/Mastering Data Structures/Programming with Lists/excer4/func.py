"""
Module to demonstrate tuple expansion.

Author: Gabriel Martinez
Date: September 26, 2020
"""


def avg(*args):   # The parameter is MISSING.  Add it back.
    """
    Returns average of all of arguments (passed via tuple expansion)

    Remember that the average of a list of arguments is the sum of all of the elements
    divided by the number of elements.

    Examples:
        avg(1.0, 2.0, 3.0) returns 2.0
        avg(1.0, 1.0, 3.0, 5.0) returns 2.5

    Parameter args: the function arguments
    Precondition: args are all numbers (int or float)
    """
    x = 0

    for i in args:
        x += i

    try:
        average = x / len(args)

    except ZeroDivisionError:
        return 0

    return average

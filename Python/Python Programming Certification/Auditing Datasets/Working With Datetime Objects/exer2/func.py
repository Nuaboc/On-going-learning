"""
A simple function comparing datetime objects.

Author: Gabriel Martinez
Date: October 13, 2020
"""
import datetime


def is_before(d1, d2):
    """
    Returns True if event d1 happens before d2.

    Values d1 and d2 can EITHER be date objects or datetime objects. If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    if type(d1) == type(d2):
        if d1 < d2:
            check = True
        else:
            check = False

    else:
        try:
            if d1.date() < d2:
                check = True
            else:
                check = False

        except AttributeError:
            if d1 == d2.date() or d1 < d2.date():
                check = True
            else:
                check = False

    return check

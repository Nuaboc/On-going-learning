"""
A simple function computing time elapsed

Author: Gabriel Martinez
Date:   October 15, 2020
"""
import datetime


def past_a_week(d1, d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.

    If d1 is after d2, or less than a week has passed, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects. If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date objects or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date objects or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    delta = datetime.timedelta(days=7)

    if type(d1) == type(d2):
        if d2 - d1 >= delta:
            check = True
        else:
            check = False
    else:
        try:
            if d2.date() - d1 >= delta:
                check = True
            else:
                check = False
        except AttributeError:
            if d2 - d1.date() >= delta:
                check = True
            else:
                check = False

    return check

"""
Functions for parsing time values from text.

While these functions are similar to functions found in the assignment, they
are missing timezone information.  The next exercise will modify these
functions to make them compatible with the assignment.

Author: Gabriel Martinez
Date: October 17, 2020
"""


def str_to_time(timestamp):
    """
    Returns the datetime object for the given timestamp (or None if the stamp is invalid)

    This function should just use the parse function in dateutil.parser to convert the
    timestamp to a datetime object.  If it is not a valid date (so the parser crashes),
    this function should return None.

    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    """
    from dateutil.parser import parse

    try:
        return parse(timestamp)
    except ValueError:
        return None


def sunset(date, daycycle):
    """
    Returns the sunset datetime (day and time) for the given date

    This function looks up the sunset from the given daycycle dictionary. If the
    daycycle dictionary is missing the necessary information, this function
    returns the value None.

    A daycycle dictionary has keys for several years (as int).  The value for each year
    is also a dictionary, taking strings of the form 'mm-dd'.  The value for that key
    is a THIRD dictionary, with two keys "sunrise" and "sunset".  The value for each of
    those two keys is a string in 24-hour time format.

    For example, here is what part of a daycycle dictionary might look like:

        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }

    Parameter date: The date to check
    Precondition: date is a date object

    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: ISO FORMAT IS 'yyyy-mm-ddThh:mm'.
    from datetime import datetime
    iso_f = date.isoformat()
    m = iso_f[5:7]
    d = iso_f[8:]

    for d1 in daycycle.keys():
        if d1 == str(date.year):
            for d2 in daycycle[d1].keys():
                if d2 == m + '-' + d:
                    time = daycycle[d1][d2]['sunset']
                    return datetime(date.year, date.month, date.day, int(time[0:2]), int(time[3:]))

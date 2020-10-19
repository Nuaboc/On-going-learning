"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: Gabriel Martinez
Date: October 18, 2020
"""
from dateutil.parser import parse
from pytz import timezone


def str_to_time(timestamp, tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)

    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.

    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and
    tz if not None, this function will assign that timezone to the datetime
    object.

    The value for tz can either be a string or a time OFFSET. If it is a string,
    it will be the name of a timezone, and it should localize the timestamp. If
    it is an offset, that offset should be assigned to the datetime object.

    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string

    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    # HINT: Use the code from the previous exercise and update the timezone
    # Use localize if timezone is a string; otherwise replace the timezone if not None

    try:
        parsed = parse(timestamp)

        if parsed.tzinfo is None and tz is not None:
            if type(tz) == str:
                return timezone(tz).localize(parsed)
            else:
                return parsed.replace(tzinfo=tz)
        else:
            return parse(timestamp)
    except ValueError:
        return None


def daytime(time, daycycle):
    """
    Returns true if the time takes place during the day.

    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dictionary.

    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.

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

    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary

    Parameter time: The time to check
    Precondition: time is a datetime object

    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    iso_f = time.isoformat()  # This method return a string
    month = iso_f[5:7]  # a string with the month of 'time' as two digits
    day = iso_f[8:10]  # a string with the day of 'time' as two digits
    dict_tz = timezone(daycycle['timezone'])

    for d1 in daycycle.keys():  # looping through the first depth of the daycycle dict
        if d1 == str(time.year):
            for d2 in daycycle[d1].keys():  # looping through the second depth of the daycycle dict
                if d2 == month + '-' + day:
                    sr = daycycle[d1][d2]['sunrise']  # a string of the hour and minutes of the sunrise
                    ss = daycycle[d1][d2]['sunset']  # a string of the hour and minutes of the sunset
                    sunrise = dict_tz.localize(str_to_time(d1 + '-' + d2 + 'T' + sr))
                    sunset = dict_tz.localize(str_to_time(d1 + '-' + d2 + 'T' + ss))
                    if sunrise < time < sunset:
                        return True
                    else:
                        return False

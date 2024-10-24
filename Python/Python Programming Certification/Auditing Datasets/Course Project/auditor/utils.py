"""
Module providing utility functions for this project.

These functions are general purpose utilities used by other modules in this project.
Some of these functions were exercises in early course modules and should be copied
over into this file.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Gabriel Martinez
Date: October 20, 2020
"""
import csv
import json
from dateutil.parser import parse
from pytz import timezone


def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    content = []
    file = open(filename)
    wrapper = csv.reader(file)

    for row in wrapper:
        line = []
        for li in row:
            line.append(li)
        content.append(line)

    file.close()

    return content


def write_csv(data, filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list of strings
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    file = open(filename, 'w', newline='')
    wrapper = csv.writer(file)

    for row in range(len(data)):
        wrapper.writerow(data[row])

    file.close()


def read_json(filename):
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents in to a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
    file = open(filename)
    data = file.read()
    content = json.loads(data)
    file.close()

    return content


def str_to_time(timestamp, tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and 
    tz if not None, this this function will assign that timezone to the datetime 
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
    indicated by the daycycle dicitionary.
    
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
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)

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


def get_for_id(id, table):
    """
    Returns (a copy of) a row of the table with the given id.
    
    Table is a two-dimensional list where the first element of each row is an identifier
    (string).  This function searches table for the row with the matching identifier and
    returns a COPY of that row. If there is no match, this function returns None.
    
    This function is useful for extract rows from a table of pilots, a table of instructors,
    or even a table of planes.
    
    Parameter id: The id of the student or instructor
    Precondition: id is a string
    
    Parameter table: The 2-dimensional table of data
    Precondition: table is a non-empty 2-dimension list of strings
    """
    for d1 in table:
        for d2 in d1:
            if d2 == id:
                copy = d1
                return copy

    return None

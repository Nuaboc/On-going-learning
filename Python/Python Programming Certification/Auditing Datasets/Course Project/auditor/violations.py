"""
Module to check violations for a flight lesson.

This module processes the primary violations, which are violations of weather restrictions. 
Weather restrictions express the minimum conditions that a pilot is allowed to fly in.  
So if a pilot has a ceiling minimum of 2000 feet, and there is cloud cover at 1500 feet, 
the pilot should not fly.To understand weather minimums, you have to integrate three 
different files: daycycle.json (for sunrise and sunset), weather.json (for hourly weather 
observations at the airport), and minimums.csv (for the schools minimums set by agreement 
with the insurance agency). You should look at those files BRIEFLY to familiarize yourself 
with them.

This module can get overwhelming if you panic and think too much about the big picture.  
Like a good software developer, you should focus on the specifications and do a little
at a time.  While these functions may seem like they require a lot of FAA knowledge, all
of the information you need is in the specifications. They are complex specifications,
but all of the information you need is there.  Combined with the provided unit tests
in tests.py, this assignment is very doable.

It may seem weird that these functions only check weather conditions at the time of 
takeoff and not the entire time the flight is in the air.  This is standard procedure 
for this insurance company.  The school is only liable if they let a pilot takeoff in 
the wrong conditions.  If the pilot stays up in adverse conditions, responsibility shifts 
to the pilot.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Gabriel Martinez
Date: October 23, 2020
"""
import utils
import pilots
import os.path
from dateutil.parser import parse


# WEATHER FUNCTIONS
def bad_visibility(visibility, minimum):
    """
    Returns True if the visibility measurement violates the minimum, False otherwise
    
    A valid visibility measurement is EITHER the string 'unavailable', or a dictionary 
    with (up to) four values: 'minimum', 'maximum',  'prevailing', and 'units'. Only 
    'prevailing' and 'units' are required; the other two are optional.The units may be 
    'FT' (feet) or 'SM' for (statute) miles, and explain how to interpret other three 
    fields, which are all floats.
    
    This function should compare the visibility 'minimum' (if it exists) against the
    minimum parameter. Else it compares the 'prevailing' visibility. This function returns
    True if minimum is more than the measurement.  If the visibility is 'unavailable', 
    then this function returns True (indicating bad record keeping).
    
    Example: Suppose we have the following visibility measurement.
        
        {
            "prevailing": 21120.0,
            "minimum": 1400.0,
            "maximum": 21120.0,
            "units": "FT"
        }
    
    This function returns True if visibility is 0.25 (miles) and False if it is 1.
    
    Parameter visibility: The visibility information
    Precondition: visibility is a valid visibility measurement, as described above.
    (e.g. either a dictionary or the string 'unavailable')
    
    Parameter minimum: The minimum allowed visibility (in statute miles)
    Precondition: minimum is a float or int
    """
    if visibility == 'unavailable':
        return True
    elif visibility['units'] == 'SM':
        if visibility['prevailing'] < minimum:
            return True
        elif visibility['prevailing'] >= minimum:
            return False
    elif visibility['units'] == 'FT':
        if visibility['minimum'] / 5280 < minimum:
            return True
        elif visibility['minimum'] >= minimum:
            return False


def bad_winds(winds, maxwind, maxcross):
    """
    Returns True if the wind measurement violates the maximums, False otherwise
    
    A valid wind measurement is EITHER the string 'calm', the string 'unavailable' or 
    a dictionary with (up to) four values: 'speed', 'crosswind', 'gusts', and 'units'. 
    Only 'speed' and 'units' are required if it is a dictionary; the other two are 
    optional.The units are either be 'KT' (knots) or 'MPS' (meters per second), and 
    explain how to interpret other three fields, which are all floats.
    
    This function should compare 'speed' or 'gusts' against the maxwind parameter (which
    ever is worse) and 'crosswind' against the maxcross. If either measurement is greater
    than the allowed maximum, this function returns True.
    
    If the winds are 'calm', then this function always returns False. If the winds are
    'unavailable', then this function returns True (indicating bad record keeping).
    
    For conversion information, 1 MPS is roughly 1.94384 knots.
    
    Example: Suppose we have the following wind measurement.
        
        {
            "speed": 12.0,
            "crosswind": 10.0,
            "gusts": 18.0,
            "units": "KT"
        }
    
    This function returns True if maxwind is 15 or maxcross is 5.  If both maxwind is 20
    and maxcross is 10, it returns False.  (If 'units' were 'MPS' it would be false in
    both cases).
    
    Parameter winds: The wind speed information
    Precondition: winds is a valid wind measurement, as described above.
    (e.g. either a dictionary, the string 'calm', or the string 'unavailable')
    
    Paramater maxwind: The maximum allowable wind speed (in knots)
    Precondition: maxwind is a float or int
    
    Paramater maxcross: The maximum allowable crosswind speed (in knots)
    Precondition: maxcross is a float or int
    """
    if winds == 'unavailable':
        return True
    elif winds == 'calm':
        return False
    elif winds['units'] == 'MPS':
        winds['speed'] = winds['speed'] * 1.94384
        winds['crosswind'] = winds['crosswind'] * 1.94384
        if 'gusts' in winds:
            winds['gusts'] = winds['gusts'] * 1.94384

    if 'gusts' in winds:
        if winds['gusts'] <= maxwind and winds['speed'] <= maxwind and winds['crosswind'] <= maxcross:
            return False
        elif winds['gusts'] > maxwind or winds['speed'] > maxwind or winds['crosswind'] > maxcross:
            return True
    elif winds['speed'] <= maxwind and winds['crosswind'] <= maxcross:
        return False
    elif winds['speed'] > maxwind or winds['crosswind'] > maxcross:
        return True


def bad_ceiling(ceiling, minimum):
    """
    Returns True if the ceiling measurement violates the minimum, False otherwise
    
    A valid ceiling measurement is EITHER the string 'clear', the string 'unavailable', 
    or a list of cloud layer measurements. A cloud layer measurement is a dictionary with 
    three required keys: 'type', 'height', and 'units'.  Type is one of 'a few', 
    'scattered', 'broken', 'overcast', or 'indefinite ceiling'.  The value 'units' must 
    be 'FT', and specifies the units for the float associated with 'height'.
    
    If the ceiling is 'clear', then this function always returns False. If the ceiling 
    is 'unavailable', then this function returns True (indicating bad record keeping).
    Otherwise, it compares the minimum allowed ceiling against the lowest cloud layer 
    that is either 'broken', 'overcast', or 'indefinite ceiling'.
    
    Example: Suppose we have the following ceiling measurement.
        
        [
            {
                "cover": "clouds",
                "type": "scattered",
                "height": 700.0,
                "units": "FT"
            },
            {
                "type": "overcast",
                "height": 1200.0,
                "units": "FT"
            }
        ]
    
    This function returns True if minimum is 2000, but False if it is 1000.
    
    Parameter ceiling: The ceiling information
    Precondition: ceiling is a valid ceiling measurement, as described above.
    (e.g. either a dictionary, the string 'clear', or the string 'unavailable')
        
    Paramater minimum: The minimum allowed ceiling (in feet)
    Precondition: minimum is a float or int
    """
    clouds = ['broken', 'overcast', 'indefinite ceiling']
    t = []

    if ceiling == 'unavailable':
        return True
    elif ceiling == 'clear':
        return False

    for x in range(len(ceiling)):
        if ceiling[x]['type'] in clouds and ceiling[x]['height'] < minimum:
            t.append(True)

    if True in t:
        return True
    else:
        return False


def get_weather_report(takeoff, weather):
    """
    Returns the most recent weather report at or before take-off.
    
    The weather is a dictionary whose keys are ISO formatted timestamps and whose values 
    are weather reports.  For example, here is an example of a (small portion of) a
    weather dictionary:
        
        {
            "2017-04-21T08:00:00-04:00": {
                "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 13.9,
                "units": "C"
            },
            "sky": [
                {
                    "cover": "clouds",
                    "type": "broken",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704211056Z"
        },
        "2017-04-21T07:00:00-04:00": {
            "visibility": {
                "prevailing": 10.0,
                "units": "SM"
            },
            "wind": {
                "speed": 13.0,
                "crosswind": 2.0,
                "units": "KT"
            },
            "temperature": {
                "value": 13.9,
                "units": "C"
            },
            "sky": [
                {
                    "type": "overcast",
                    "height": 700.0,
                    "units": "FT"
                }
            ],
            "code": "201704210956Z"
        }
        ...
    },
    
    If there is a report whose timestamp matches the ISO representation of takeoff, 
    this function uses that report.  Otherwise it searches the dictionary for the most
    recent report before takeoff.  If there is no such report, it returns None.
    
    Example: If takeoff was as 8 am on April 21, 2017 (Eastern), this function returns 
    the value for key '2017-04-21T08:00:00-04:00'.  If there is no additional report at
    9 am, a 9 am takeoff would use this value as well.
    
    Parameter takeoff: The takeoff time
    Precondition: takeoff is a datetime object
    
    Paramater weather: The weather report dictionary 
    Precondition: weather is a dictionary formatted as described above
    """
    import datetime

    tot = takeoff.isoformat()
    delta = datetime.timedelta(hours=1)

    if takeoff.minute != 00:
        new_tot = tot[0:14] + '00' + tot[16:]
        if new_tot in weather:
            return weather[new_tot]
        else:
            new_date = parse(new_tot) - delta
            for x in range(len(weather)):
                if new_date.isoformat() in weather:
                    return weather[new_date.isoformat()]
                else:
                    new_date = new_date - delta

    if tot in weather:
        return weather[tot]
    else:
        date = takeoff - delta
        for x in range(len(weather)):
            if date.isoformat() in weather:
                return weather[date.isoformat()]
            else:
                date = date - delta


def get_weather_violation(weather, minimums):
    """
    Returns a string representing the type of weather violation (empty string if flight is ok)
    
    The weather reading is a dictionary with the keys: 'visibility', 'wind', and 'sky'.
    These correspond to a visibility, wind, and ceiling measurement, respectively. It
    may have other keys as well, but these can be ignored. For example, this is a possible 
    weather value:
        
        {
            "visibility": {
                "prevailing": 21120.0,
                "minimum": 1400.0,
                "maximum": 21120.0,
                "units": "FT"
            },
            "wind": {
                "speed": 12.0,
                "crosswind": 3.0,
                "gusts": 18.0,
                "units": "KT"
            },
            "temperature": {
                "value": -15.6,
                "units": "C"
            },
            "sky": [
                {
                    "cover": "clouds",
                    "type": "broken",
                    "height": 2100.0,
                    "units": "FT"
                }
            ],
            "weather": [
                "light snow"
            ]
        }
    
    The minimums is a list of the four minimums ceiling, visibility, and max windspeed,
    and max crosswind speed in that order.  Ceiling is in feet, visibility is in statute
    miles, max wind and cross wind speed are both in knots. For example, 
    [3000.0,10.0,20.0,8.0] is a potential minimums list.
    
    This function uses bad_visibility, bad_winds, and bad_ceiling as helpers. It returns
    'Visibility' if the only problem is bad visibility, 'Wind' if the only problem is 
    wind, and 'Ceiling' if the only problem is the ceiling.  If there are multiple
    problems, it returns 'Weather', It returns 'Unknown' if no weather reading is 
    available (e.g. weather is None).  Finally, it returns '' (the empty string) if 
    the weather is fine and there are no violations.
    
    Parameter weather: The weather measure
    Precondition: weather is dictionary containing a visibility, wind, and ceiling measurement,
    or None if no weather reading is available.
    
    Parameter minimums: The safety minimums for ceiling, visibility, wind, and crosswind
    Precondition: minimums is a list of four floats
    """
    if weather is None:
        return 'Unknown'

    a = bad_visibility(weather['visibility'], minimums[1])
    b = bad_winds(weather['wind'], minimums[2], minimums[3])
    c = bad_ceiling(weather['sky'], minimums[0])
    d = [a, b, c]
    e = []

    if d[0]:
        e.append('Visibility')
    if d[1]:
        e.append('Winds')
    if d[2]:
        e.append('Ceiling')

    if len(e) > 1:
        return 'Weather'
    elif len(e) == 1:
        return e[0]
    elif len(e) == 0:
        return ''


# FILES TO AUDIT
# Sunrise and sunset
DAYCYCLE = 'daycycle.json'
# Hourly weather observations
WEATHER = 'weather.json'
# The list of insurance-mandated minimums
MINIMUMS = 'minimums.csv'
# The list of all registered students in the flight school
STUDENTS = 'students.csv'
# The list of all take-offs (and landings)
LESSONS = 'lessons.csv'


def list_weather_violations(directory):
    """
    Returns the (annotated) list of flight reservations that violate weather minimums.
    
    This function reads the data files in the given directory (the data files are all
    identified by the constants defined above in this module).  It loops through the
    list of flight lessons (in lessons.csv), identifying those takeoffs for which
    get_weather_violation() is not the empty string.
    
    This function returns a list that contains a copy of each violating lesson, together 
    with the violation appended to the lesson.
    
    Example: Suppose that the lessons
        
        S00687  548QR  I061  2017-01-08T14:00:00-05:00  2017-01-08T16:00:00-05:00  VFR  Pattern
        S00758  548QR  I072  2017-01-08T09:00:00-05:00  2017-01-08T11:00:00-05:00  VFR  Pattern
        S00971  426JQ  I072  2017-01-12T13:00:00-05:00  2017-01-12T15:00:00-05:00  VFR  Pattern
    
    violate for reasons of 'Winds', 'Visibility', and 'Ceiling', respectively (and are the
    only violations).  Then this function will return the 2d list
        
        [[S00687, 548QR, I061, 2017-01-08T14:00:00-05:00, 2017-01-08T16:00:00-05:00, VFR, Pattern, Winds],
         [S00758, 548QR, I072, 2017-01-08T09:00:00-05:00, 2017-01-08T11:00:00-05:00, VFR, Pattern, Visibility],
         [S00971, 426JQ, I072, 2017-01-12T13:00:00-05:00, 2017-01-12T15:00:00-05:00, VFR, Pattern, Ceiling]]
    
    REMEMBER: VFR flights are subject to minimums with VMC in the row while IFR flights 
    are subject to minimums with IMC in the row.  The examples above are all VFR flights.
    If we changed the second lesson to
    
        S00758, 548QR, I072, 2017-01-08T09:00:00-05:00, 2017-01-08T11:00:00-05:00, IFR, Pattern
    
    then it is possible it is no longer a visibility violation because it is subject to
    a different set of minimums.
    
    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', and 'lessons.csv'
    """
    # Load in all of the files
    f_l_path = os.path.join(directory, LESSONS)
    lessons = utils.read_csv(f_l_path)
    f_m_path = os.path.join(directory, MINIMUMS)
    minimums = utils.read_csv(f_m_path)
    f_s_path = os.path.join(directory, STUDENTS)
    students = utils.read_csv(f_s_path)
    f_dc_path = os.path.join(directory, DAYCYCLE)
    daycycle = utils.read_json(f_dc_path)
    f_w_path = os.path.join(directory, WEATHER)
    weather = utils.read_json(f_w_path)

    instructed = False
    vfr = False

    result = []

    for lesson in lessons[1:]:
        # Get the takeoff time
        #tz = parse(lesson[3]).tzinfo  # tz from the lesson takeoff
        #takeoff = utils.str_to_time(lesson[3], tz)  # A datetime object

        #daytime = utils.daytime(parse(lesson[3]), daycycle)  # If takeoff was during day or night
        takeoff = utils.str_to_time(lesson[3],daycycle['timezone'])
        landing = utils.str_to_time(lesson[4],daycycle['timezone'])
        daytime  = utils.daytime(takeoff,daycycle) and utils.daytime(landing,daycycle)





        '''#Dylan: this isn't necessary
        dates = []

        for dt in range(3, len(student)):
            if student[dt] != '' and isinstance(parse(student[dt]), type(parse(takeoff.isoformat()))):
                dtw = parse(student[dt]).replace(tzinfo=tz)  # datetime with tz info
                dates.append(dtw.isoformat())  # Add datetime in iso  format
            else:
                dates.append(student[dt])  # Add the rest of the values without dates

        id = student[:3]  # A list slice from student with the id number, first name and last name
        student = id + dates  # Concatenate lists
        ifr = pilots.has_instrument_rating(takeoff, student)
        '''

        # Get the pilot credentials
        student = utils.get_for_id(lesson[0], students)  # A row of a pilot with his or her credentials
        cert = pilots.get_certification(takeoff, student)



        # Get the pilot minimums
        #if lesson[2] != '':
        #    instructed = True
        #you are missing the false condition
        teacher = lesson[2]
        instructed = teacher != ''

        #missing false condiiton
        #if lesson[5] == 'VFR':
        #    vfr = True
        vfr = lesson[5] == 'VFR'

        pilot_min = pilots.get_minimums(cert, lesson[6], instructed, vfr, daytime, minimums)
        # Get the weather conditions
        w_report = get_weather_report(takeoff, weather)
        # Check for a violation and add it to the list if so
        check = get_weather_violation(w_report, pilot_min)

        if check != '':
            lesson.append(check)
            result.append(lesson)

    return result

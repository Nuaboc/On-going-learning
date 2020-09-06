"""
A function to extract names from e-mail addresses.

Author: Gabriel Martinez
Date: August 28, 2020
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.

    We assume (see the precondition below) that the e-mail address is in one of
    two forms:

        last.first@megacorp.com
        first.last@mompop.net

    where first and last correspond to the person's first and last name.  Names
    are not empty, and contain only letters. Everything after the @ is guaranteed
    to be exactly as shown.

    The function preserves the capitalization of the e-mail address.

    Examples:
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'

    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    if s[-3:] == 'com':
        a = introcs.find_str(s, '@')
        b = introcs.find_str(s[:a], '.') + 1
        first = s[b:a]

    else:
        a = introcs.find_str(s, '@')
        b = introcs.find_str(s[:a], '.')
        first = s[:b]

    return first

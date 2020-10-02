"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Gabriel Martinez
Date: September 15, 2020
"""
import introcs


def findall(text, sub):
    """
    Returns the tuple of all positions of substring sub in text.

    If sub does not appears anywhere in text, this function returns the empty tuple ().

    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)

    Parameter text: The text to search
    Precondition: text is a string

    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    all_pos = ()
    start = 0

    while True:
        print('starting loop')
        find = introcs.find_str(text, sub, start)
        if find >= 0:
            print('Found "' + sub + '" in position ' + str(find))
            all_pos += (find,)
            start = find + 1

        print(all_pos)

        if find == -1:
            return all_pos

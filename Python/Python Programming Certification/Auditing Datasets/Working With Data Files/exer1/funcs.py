"""
Functions for simple reading to and writing from a file.

Author: Gabriel Martinez
Date:   October 7, 2020
"""


def count_lines(filepath):
    """
    Returns the number of lines in the given file.

    Lines are separated by the '\n' character, which is standard for Unix files.

    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    # HINT: Remember, you can use a file in a for-loop
    file = open(filepath)
    result = 0

    for line in file:
        result += 1

    file.close()

    return result


def write_numbers(filepath, n):
    """
    Writes the numbers 0..n-1 to a file.

    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character,
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'

    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file

    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
    file = open(filepath, 'w')
    x = 0
    file.write(str(x))

    for i in range(n):
        print('here')
        x += 1
        file.write('\n' + str(x))

    print('line 54')

    file.close()

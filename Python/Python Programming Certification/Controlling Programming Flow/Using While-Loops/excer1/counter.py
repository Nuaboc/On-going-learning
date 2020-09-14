"""
Module demonstrating an input-driven while loop

There is no test script for this module.  Run this module as a script to test it.

Author: Gabriel Martinez
Date: September 13, 2020
"""


def count_inputs():
    """
    Returns the number of times the user chose to continue.

    This function repeated asks the user

        Keep going [y/n]?

    If the user answers 'y', the function adds one to a counter and keeps going.
    If the user answers 'n', the function quits and returns the number of times
    that the user answered 'y'.  If the user answers anything else, the function
    responds with

        Answer unclear. Use 'y' or 'n'.

    It will not quit in this case, but it will not add to the counter either.
    """
    counter = 0
    going_on = True
    while going_on:
        try:
            ask = input('Keep going [y/n]? ')
            if ask == 'y':
                counter += 1
            elif ask == 'n':
                return counter
            else:
                z = ask / 1
        except Exception:
            print("Answer unclear. Use 'y' or 'n'.")


# Script code to test the function
# DO NOT MODIFY BELOW THIS LINE
if __name__ == '__main__':
    result = count_inputs()
    plural = ' time.' if result == 1 else ' times.'
    print("You answered 'y' "+str(result)+plural)

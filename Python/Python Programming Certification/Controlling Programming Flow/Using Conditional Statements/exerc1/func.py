"""
A function to search for the first vowel position

Author: Gabriel Martinez
Date: August 26, 2020
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns len(s) if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns 4
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    # assert len(s) >= 1

    # result will have the len() of s or the index of the lowest indexed vowel
    result = len(s)

    # Each check_"vowel" will have its vowel index from s or -1.
    check_a = introcs.find_str(s, 'a')
    check_e = introcs.find_str(s, 'e')
    check_i = introcs.find_str(s, 'i')
    check_o = introcs.find_str(s, 'o')
    check_u = introcs.find_str(s, 'u')
    check_y = introcs.find_str(s, 'y', 1)

    if check_a > -1:
        result = check_a

    if result > check_e > -1:
        result = check_e

    if result > check_i > -1:
        result = check_i

    if result > check_o > -1:
        result = check_o

    if result > check_u > -1:
        result = check_u

    if result > check_y > -1:
        result = check_y

    return result


print(first_vowel('yyng'))

import introcs


def second_in_list(s):
    """
    Returns: the second item in comma-separated list

    The final result should not have any whitespace around the edges.

    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list('  do  ,  re  ,  me  ,  fa  ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'

    Parameter s: The list of items
    Precondition: s is a string of at least three items separated by commas.
    """
    before = len(s[:introcs.find_str(s, ",")])
    after = len(s[:introcs.find_str(s[before + 1:], ',')])
    slice = s[before + 1:after + before + 1]
    result = introcs.strip(slice)
    return result


print(second_in_list('apple, banana, orange'))

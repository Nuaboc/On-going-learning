import introcs


def initials(n):
    """
    specification
    :param n:
    :return:
    """
    first = n[0]
    pos = len(n[:introcs.find_str(n, " ")]) + 1
    last = n[pos]
    result = first + ". " + last + "."
    return result


print(initials('Walter White'))

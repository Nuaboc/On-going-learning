import random


def rollem(first, last):
    """
    Returns the sum of two random numbers.

    The numbers generated are between first and last (inclusive).

    Example: rollem(1,6) can return any value between 2 and 12.

    Parameter first: The lowest possible number
    Precondition: first is an integer

    Parameter last: The greatest possible number
    Precondition: last is an integer, last >= first
    """

    return random.randint(first, last) + random.randint(first, last)

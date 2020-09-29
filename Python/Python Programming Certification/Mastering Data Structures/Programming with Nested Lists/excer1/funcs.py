"""
Module demonstrating immutable functions on nested lists.

All of these functions make use of accumulators that make new lists.

Author: Gabriel Martinez
Date: September 28, 2020
"""


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only numbers in it.

    Examples:
        row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) returns [0.9, 1.5, 1.7]
        row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.
    """
    result = []

    for d1 in table:
        inside = 0

        for d2 in d1:
            inside += d2

        result.append(inside)

    return result


def crossout(table, row, col):
    """
    Returns a copy of the table, missing the given row and column.

    Examples:
        crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
        crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
        crossout([[1,3],[6,2]],0,0) returns [[2]]
        crossout([[6]],0,0) returns []

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the column to remove
    Precondition: col is an index (int) for a column of table
    """
    copy = []
    x = 0
    y = 0

    for d1 in table:  # d1 represents each value in first depp of table.
        print('for d1 in table:')
        print(x)

        if x != row:
            print('if x != row: passed')
            inside = []
            for d2 in d1:  # d2 represents each value in the second depp in table.
                print('for d2 in d1:')
                print(y)
                if y != col:
                    print('if y != col: passed')
                    inside.append(d2)
                    print(inside)
                y += 1
            copy.append(d1)
        x += 1

    return copy


table1 = [[0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [1.5, 2.3, 0.4]]
print(crossout(table1, 1, 2))

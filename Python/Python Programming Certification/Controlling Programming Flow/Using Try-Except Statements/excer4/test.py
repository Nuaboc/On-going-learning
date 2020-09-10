"""
A test script for the function iso_8601.

Author: Gabriel Martinez
Date: September 10, 2020
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')

    # Put your test cases here
    result = func.iso_8601('00:00:00')
    introcs.assert_equals(True, result)

    # Without wrong colon quantity
    result = func.iso_8601('000000')
    introcs.assert_equals(False, result)

    result = func.iso_8601('00:0000')
    introcs.assert_equals(False, result)

    result = func.iso_8601('00:00:00:00')
    introcs.assert_equals(False, result)

    # Wrong hour
    result = func.iso_8601('48:00:00')
    introcs.assert_equals(False, result)
    
    result = func.iso_8601('-3:00:00')
    introcs.assert_equals(False, result)

    # Wrong minute
    result = func.iso_8601('00:72:00')
    introcs.assert_equals(False, result)
    
    result = func.iso_8601('00:-05:00')
    introcs.assert_equals(False, result)

    # Wrong second
    result = func.iso_8601('00:00:90')
    introcs.assert_equals(False, result)
    
    result = func.iso_8601('00:00:-38')
    introcs.assert_equals(False, result)

    # Too many digits
    result = func.iso_8601('100:004:090')
    introcs.assert_equals(False, result)

    # Empty
    result = func.iso_8601('')
    introcs.assert_equals(False, result)


if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')

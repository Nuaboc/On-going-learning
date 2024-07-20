"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Gabriel Martinez
Date:   August 1, 2020
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")

    # Test Cases
    result = currency.before_space('Hello World!')
    introcs.assert_equals('Hello', result)

    result = currency.before_space(' one')
    introcs.assert_equals('', result)

    result = currency.before_space('1, 2, 3, 4, 5')
    introcs.assert_equals('1,', result)

    result = currency.before_space('Bye!   Adios!')
    introcs.assert_equals('Bye!', result)


def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    # Test Cases
    result = currency.after_space('Hello World!')
    introcs.assert_equals('World!', result)

    result = currency.after_space('two ')
    introcs.assert_equals('', result)

    result = currency.after_space('1, 2, 3, 4, 5')
    introcs.assert_equals('2, 3, 4, 5', result)

    result = currency.after_space('Good   bye!')
    introcs.assert_equals('  bye!', result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    # Test Cases
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('"A B C"')
    introcs.assert_equals('A B C', result)

    result = currency.first_inside_quotes('""')
    introcs.assert_equals('', result)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")

    # Test Cases
    result = currency.get_src('{"success": true, "src": "2 United States '+\
                              'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src('{"success":false,"src":"","dst":"",'+\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_src('{"success": true, "src":"2 United States '+\
                              'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":false,"src": "","dst":"",'+\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")

    # Test Cases
    result = currency.get_dst('{"success": true, "src": "2 United States '+\
                              'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst('{"success":false,"src":"","dst": "",'+\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_dst('{"success": true, "src":"2 United States '+\
                              'Dollars", "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst('{"success":false,"src": "","dst":"",'+\
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")

    # Test Cases
    result = currency.has_error('{"success": true, "src": "2 United States '+\
                                'Dollars", "dst": "1.772814 Euros", "error":""}')
    introcs.assert_false(result)

    result = currency.has_error('{"success":false,"src":"","dst": "",'+\
                                '"error":"Source currency code is invalid."}')
    introcs.assert_true(result)

    result = currency.has_error('{"success": true, "src":"2 United States '+\
                                'Dollars", "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_false(result)

    result = currency.has_error('{"success":false,"src": "","dst":"",'+\
                                '"error": "Source currency code is invalid."}')
    introcs.assert_true(result)


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")

    # Test Cases
    result = currency.service_response('USD', 'EUR', 2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States '+\
                          'Dollars", "dst": "2.2160175 Euros", "error": ""}',
                          result)

    result = currency.service_response('USB', 'BBD', 5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '+\
                          '"The rate for currency USB is not present."}', result)

    result = currency.service_response('EUR', 'LOL', 2)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '+\
                          '"The rate for currency LOL is not present."}', result)

    result = currency.service_response('IRR', 'LSL', -1)
    introcs.assert_equals('{"success": true, "src": "-1.0 Iranian Rial", '+\
                          '"dst": "-0.00033250207813798836 Lesotho Maloti", '+\
                          '"error": ""}', result)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")

    # Test Cases
    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)

    result = currency.iscurrency('USB')
    introcs.assert_equals(False, result)


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")

    # Test Cases
    result = currency.exchange('USD', 'EUR', 9)
    introcs.assert_floats_equal(7.977663, result)

    result = currency.exchange('AOA', 'AMD', -3)
    introcs.assert_floats_equal(-4.136006348132634, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print("All tests completed successfully.")

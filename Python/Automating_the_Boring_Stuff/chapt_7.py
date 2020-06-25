# Chapter 7
# Pattern Matching With Regular Expressions

import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

match_obj = phone_num_regex.search('My number is 415-550-4322.')

print("Phone number found: " + match_obj.group())

print(match_obj.group())

print('.........................................................')

ph_n_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
test_file = 'regex_test.txt'

with open(test_file) as tf:
    a = ph_n_regex.findall(tf.read())
    for i in a:
        print("Phone numbers on text: " + str(i))

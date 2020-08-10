"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Gabriel Martinez
Date:   August 1, 2020
"""

import currency

org = input('3-letter code for original currency: ')

new = input('3-letter code for the new currency: ')

amt = input('Amount of the original currency: ')

print('You can exchange ' + amt + ' ' + org + ' ' + 'for ' +
      str(round(currency.exchange(org, new, float(amt)), 3)) + ' ' + new + '.')

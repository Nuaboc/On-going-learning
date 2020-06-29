# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Enhanced Unit Converter


def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')


def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(round(miles, 2)))


def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(round(km, 2)))


def kilograms_pounds():
    kilograms = ''
    lb = kilograms
    print('Mass in pounds: {0}'.format(lb))


def pounds_kilograms():
    pounds = ''
    kg = pounds
    print('Mass in kilograms: {0}'.format(kg))


def celsius_fahrenheit():
    celsius = ''
    f = celsius
    print('Temperature in Fahrenheit: {0}'.format(f))


def fahrenheit_celsius():
    fahrenheit = ''
    c = fahrenheit
    print('temperature in Celsius: {0}'.format(c))


if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice == '1':
        km_miles()
    elif choice == '2':
        miles_km()
    elif choice == '3':
        kilograms_pounds()
    elif choice == '4':
        pounds_kilograms()
    elif choice == '5':
        celsius_fahrenheit()
    elif choice == '6':
        fahrenheit_celsius()

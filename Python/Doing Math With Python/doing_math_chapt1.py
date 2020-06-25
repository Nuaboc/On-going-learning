# Doing Math With Python
# Chapter 1 Working With Numbers

n = 25.5 * 2.54 / 100

print(n)

print(round(n, 4))

f = 98.6

c = 37

fahrenheit = c * 9/5 + 32

celsius = f - 32 * 5/9

print(fahrenheit)
print(celsius)

# .........................................................................

# Programming Challenges

# Even-Odd Machine

on = True


def check_num():
    """"Verify if the number is even or odd."""
    while True:
        num = int(input("Enter a number: "))

        try:
            if num % 2 == 0:
                print('Even')
                break
            elif num % 2 == 1:
                print('Odd')
                break
        except ValueError:
            print('Enter only numbers!!!')


def ask():
    global on
    while True:
        print("wanna try again? type yes/no")
        answer = input()

        if answer == 'yes':
            break
        elif answer == 'no':
            on = False
            break
        else:
            continue


while on:
    check_num()
    ask()


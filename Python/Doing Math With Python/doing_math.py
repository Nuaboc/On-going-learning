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

# .................................................................................

# Programming Challenges

# Even-Odd Machine


def check_num():
    """"Verify if the number is even or odd."""
    num = input("Enter a number: ")

    x = int(num)
    if x % 2 == 0:
        print('Even')
    elif x % 2 == 1:
        print('Odd')
    elif x.is_
        print('Enter a number!')


def ask():
    print("wanna try again? type yes/no")
    global y
    y = input()


while 1:
    check_num()
    ask()

    if y == 'yes':
        continue
    elif y == 'no':
        break
    else:
        ask()

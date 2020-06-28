# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Even-Odd Vending Machine

on = True


def check_num():
    """"Verify if the number is even or odd."""
    while True:
        num = input("Enter a number: ")

        try:
            if int(num) % 2 == 0:
                print('Even')
                for i in range(20):
                    if i % 2 == 0:
                        print(int(num) + i)
                        print("this")
                break

            elif int(num) % 2 == 1:
                print('Odd')
                for i in range(20):
                    if i % 2 == 1:
                        print(int(num) + i)
                        print("that")
                break

        except ValueError:
            print('Enter only numbers!!!')


def ask():
    """Ask the user if he/she want to try again or end the program."""
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

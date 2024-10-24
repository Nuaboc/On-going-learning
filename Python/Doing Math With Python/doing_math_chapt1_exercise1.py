# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Even-Odd Vending Machine


import matplotlib.pyplot as plt

x_nums = range(1, 11)
y_nums = []

# plt.plot(x_nums, y_nums)


on = True


def check_num():
    """"Verify if the number is even or odd."""
    while True:
        num = input("Enter a number: ")

        try:
            if round(float(num)) % 2 == 0:
                print('Even')
                # print the next 9 'even' numbers.
                for i in range(20):
                    if i % 2 == 0:
                        print(round(float(num)) + i)
                        y_nums.append(round(float(num)) + i)
                plt.plot(x_nums, y_nums)
                plt.show()

                break

            elif round(float(num)) % 2 == 1:
                print('Odd')
                # print the next 9 'odd' numbers.
                for i in range(20):
                    if i % 2 == 0:
                        print(round(float(num)) + i)
                        y_nums.append(round(float(num)) + i)
                plt.plot(x_nums, y_nums)
                plt.show()

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

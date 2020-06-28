# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Enhanced Multiplication Table Generator


def multi_table(a):

    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a, i, a*i))


if __name__ == '__main__':
    a = input('Enter a number: ')
    multi_table(int(a))

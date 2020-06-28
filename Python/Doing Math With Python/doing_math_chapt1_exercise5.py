# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Give Exit Power to the User


"""
Run until exit layout
"""


def fun():
    print('I am in an endless loop')


if __name__ == '__main__':
    while True:
        fun()
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break

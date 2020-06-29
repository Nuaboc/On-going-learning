# Doing Math With Python
# Chapter 1 Working With Numbers
# Programming Challenges

# Enhanced Multiplication Table Generator


def multi_table(x, y):
    """By giving 2 arguments, this functions return a table with the quantity of multiples given."""
    y += 1

    for i in range(1, y):
        print('{0} x {1} = {2}'.format(x, i, x*i))


if __name__ == '__main__':
    print('Which table would you like to see?')
    num = input('Enter a number: ')
    
    # Ask up to how many multiples
    print("Up to how many multiples of " + num + "?")
    how_many = input('Enter a number: ')
    multi_table(int(num), int(how_many))

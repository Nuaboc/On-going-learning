# 10.6 to 10.7

first_num = input("Give me one number: ")

sec_num = input("Give me a second number: ")

try:
    result = int(first_num) + int(sec_num)
except ValueError:
    print("Please, enter only numbers!")
else:
    print(result)

print(".......................................")

while True:
    first_num = input("Give me a number: ")

    sec_num = input("Give me a second number: ")

    try:
        result = int(first_num) + int(sec_num)
    except ValueError:
        print("Please, enter only numbers!")
    else:
        print(result)

    keep_going = input("Want to let other user to put numbers? (y or n) ")

    if keep_going == 'n':
        break
    # here the else statement is not necessary because it will continue automatically with the while loop

# 10.3 guest

ti = "What is your name? "
to = "And your last name? "

input(ti)
input(to)

while True:
    name = input(ti)

    if name == 'quit':
        break
    else:
        continue

    last = input(to)

    if last == 'quit':
        break
    else:
        print("Welcome, " + name.title() + ' ' + last.title() + "!")
        with open('guest.txt', 'a') as guest_book:
            guest_book.write(name.title() + ' ' + last.title())


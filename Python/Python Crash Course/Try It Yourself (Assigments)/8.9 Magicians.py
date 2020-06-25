# 8.9 - 8.11


def show_magicians(x):
    # the x parameter let me use any list that I want
    for m_n in x:
        print(m_n.title())


magician_names = ['smith', 'pepe', 'pepito', 'ramon']
graduates = []


def make_great(magician_names):
    while magician_names:
        school = magician_names.pop()
        print(school.title() + ' is learning.')
        graduates.append(school.title() + ", the Great!")


show_magicians(magician_names)

print()

make_great(magician_names[:])

print()

print(graduates)

print(magician_names)

print()

show_magicians(graduates)
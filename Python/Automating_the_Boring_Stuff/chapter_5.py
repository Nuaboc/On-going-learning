# chapter 5
# the get method for dictionaries

my_dict = {'name': 'pepe', 'last': 'lepoo', 'color': 'black', 'age': 19}

print("His name is " + my_dict.get('name', 'pepa').title() + " " + my_dict.get('last', 'pig').title() + ".")

print("It is " + my_dict.get('color', 'pink') + " and has " + str(my_dict.get('age', 5)) + " years.")

print("..............................................")

if 'place' not in my_dict:
    my_dict['place'] = 'usa'

print(my_dict)
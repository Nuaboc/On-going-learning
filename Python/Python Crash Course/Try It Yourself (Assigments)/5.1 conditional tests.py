hero = 'batman'
print ("Is hero == 'batman'? I predict True.")
print (hero == 'batman')

print ("\nIs hero == 'super-man'? I predict False")
print (hero == 'super-man')

num1 = 10
print ("\nIs num1 == 10? I predict True")
print (num1 == 10)

num15 = 150
print ("\nWill be False")
print (num15 == 15)

cetera = 1
print ("\nWill be True")
print (cetera == 1)

h1 = 'House'
print ("\nIn 'house' will be False")
print (h1 == 'house')

# This last is False because Python is case sensitive

h2 = 'home'
print ("\nIn 'home' will be True")
print (h2 == "HoME".lower())

h3 = "Home Sweet Home"
print ("\nIn 'Home Sweet Home' will be also True.")
print (h3 == 'home sweet home'.title())
# The .title() method display EACH WORD in titlecase!

food1 = 'pollo'
food2 = 'pavo'
food3 = 'pernil'
print ("\nIn 'foods' will be False then True")
print (food1 == 'pollo' and food3 == 'arroz')
print (food2 == 'pavo' or food4 == 'arroz')

color1 = 'red'
color2 = 'blue'
color3 = 'yellow'
print ("\nIn 'colors', first will be True, then False")
print (color2 == 'blue' and color1 == 'red')
print (color3 == 'green' or color1 == 'yellow')

list1 = [2, 4, 8, 10]
if 6 in list1:
	print('\nlist1 True')

if 2 in list1:
	print('\nTrue')

list2 = ['red', 'blue', 'green', 'yellow']
if 'red' in list2:
	print('\nTrue')
elif 'orange' in list2:
	print("False")

if 'red' in list2:
	print ('\nyeah')

if 'red' not in list2:
	print ('bah')
else:
	print ('eso es')

if 'purple' in list2:
	print ('cool')
else:
	print ("Would be nice")

if 'yellow' not in list2:
	print ("Missing the sun.")
elif 'red' in list2:
	print ("I'm cool with red.")
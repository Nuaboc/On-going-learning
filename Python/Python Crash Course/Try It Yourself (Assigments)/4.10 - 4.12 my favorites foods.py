# exerc 4.11

my_pizzas = ['boricua', 'italiana', 'stuff crust']
print (my_pizzas)

friend_pizzas = my_pizzas[:]

my_pizzas.append('meat lovers')
friend_pizzas.append('rusa')

print ("\nMy pizzas could be:")
for my_pizza in my_pizzas:
	print (my_pizza)

print ("\nMy friend prefers:")
for my_pizza in friend_pizzas:
	print (my_pizza)
# inicialmente my_pizza tiene el valor de la lista my_pizzas segun el loop, se pudo haber utilizado otra variable en el loop de las pizzas de mi amigo, pero al re-utilizarse my_pizza, su valor cambia a la lista friend_pizzas

# exercise 4.10

animals = ['chameleon', 'dog', 'cat', 'monkey', 'bear']
print ("\nThe first three items in the list are:")
for animal in animals[:3]:
	print (animal)

print ("\nThree items form the middle of the list are:")
for animal in animals[1:4]:
	print (animal)

print ("\nThe last three items from the list are:")
for animal in animals[2:]:
	print (animal)

print (my_pizza)
# my_pizza tiene el valor de 'rusa' ya que es el ultimo valor que se la da en el loop de friend_pizzas

print (my_pizzas[1:3])
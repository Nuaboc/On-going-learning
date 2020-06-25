# this is a tuple (an unchangeable list)

buffet = ("spaguetti", "rice and beans", "mofongo", "pollo asado",
	"papas fritas")
print ("The restaurant offers:")
for food in buffet:
	print (food.title())

buffet = ("rice and beans", "mofongo", "pollo asado", "papas majadas",
	"arroz con dulce")
print ("\nNow the restaurant offers:")
for food in buffet:
	print (food.title())
	
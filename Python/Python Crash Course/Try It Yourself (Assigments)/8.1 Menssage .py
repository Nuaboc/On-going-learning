# 8.1 Menssage y 8.2

def display_message():
    # Esto es una funcion sencilla que produce un saludo.
    print("Yo estoy aprendiendo a hacer funciones en Python.")

display_message()

def libro_favorito(title):
    print("\nUno de mis libros favoritos es " + title.title() + ".")

# no es necesario poner print antes de la funcion ex. print(libro_favorito())
# porque ya dentro de la funcion hay un print. Ademas printeiaria un 'NONE' innecesario.

libro_favorito('Salvaje de Corazon')

libro_favorito('maze runner')

libro_favorito('juan')

# 7.10 Dream Vacation

respuestas = {}

sondeo_activo = True

while sondeo_activo:

    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    respuestas[name] = response


    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        sondeo_activo = False


print ("\n---Resultados de la Encuesta---")
for name, response in respuestas.items():
    print(name.title() + " would like to climb " + response.title() + ".")


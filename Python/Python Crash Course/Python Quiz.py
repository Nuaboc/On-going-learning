import easygui as eg

# SETTING THINGS UP (only need this once)

eg.msgbox("¡Bienvenido al super Quiz!")

score = 0


# QUESTION 1[]

answers = ["A bird","A plane","Superman","A house","A horse"] 


choice = eg.buttonbox("What is this?","¡Super Quiz!",answers,"house.gif") 

if choice == "A house":
    eg.msgbox("Well done!","¡Super Quiz!")
    score = score + 1
else:
    eg.msgbox("Wrong, it's a house!","¡Super Quiz!")


# Pregunta 2

answers = ["Push UP","Squad","Cuica","Pull UP","Squat"]


choice = eg.buttonbox("¿Cual es el nombre de este ejercicio?","Super ¡Quiz!",answers,"squat.gif")

if choice == "Squat":
	eg.msgbox("¡Muy bien!","¡Super Quiz!")
	score = score + 1
else:
	eg.msgbox("¿Qué te pasa? ¡Se llama Squat!","¡Super Quiz!")


# Pregunta 3

answers = ["arroz","mayonesa","brownie","gato","miel"]

choice = eg.buttonbox("¿Qué es eso?","Super ¡Quiz!",answers,"brownie.gif")

if choice == "brownie":
	eg.msgbox("¡Muy bien!","¡Super Quiz!")
	score = score + 1
else:
	eg.msgbox("¡Nada que ver! ¡Eso es un brownie!","¡Super Quiz!")


# Pregunta 4

answers = ["flaco","musculoso","obeso","cangri","sin piel"]

choice = eg.buttonbox("¿Cómo esta este hombre estéticamente?","Super ¡Quiz!",answers,"muscular.gif")

if choice == "musculoso":
	eg.msgbox("¡Muy bien!","¡Super Quiz!")
	score = score + 1
else:
	eg.msgbox("No. ¡Esta musculoso!","¡Super Quiz!")


# Pregunta 5

answers = ["Football","Cricket","Rugby","Hockey","Banana racing"] 


choice = eg.buttonbox("What sport is this?","¡Super Quiz!",answers,"football.gif") 

if choice == "Football":
    eg.msgbox("Well done!","¡Super Quiz!")
    score = score + 1
else:
    eg.msgbox("Wrong, is Football!","¡Super Quiz!")


if score == 5:
    eg.msgbox("Sacaste A+ ¡Muy bien!","¡Super Quiz!")
else:
    score <3
    eg.msgbox ("You loser!!!","¡Super Quiz!")





# END

eg.msgbox("Well done, you scored " + str(score))

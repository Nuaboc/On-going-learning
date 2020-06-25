# 7.5 Movie Tickets

prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' to finish."

activo = True

while activo:
    age = input(prompt)

    if age == 'quit':
        activo = False
    else:
        age = int(age)
        if age <= 3:
             print("Your ticket is free.")
        elif age <= 12:
           print("Your ticket price is $10.")
        else:
           print("Your ticket price is $15.")

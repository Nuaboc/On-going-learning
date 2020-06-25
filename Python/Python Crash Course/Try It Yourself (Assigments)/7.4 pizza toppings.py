# 7.4 Pizza Toppings

prompt = "\nPlease, enter a topping you would like to add to your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "
prompt += "\nRecuerda add chocolate."

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("Adding " + topping + " to your pizza.")

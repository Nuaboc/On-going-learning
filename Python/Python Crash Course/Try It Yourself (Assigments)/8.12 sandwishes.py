# 8.12


def sandwich_orders(*toppings):
    print("Making a sandwich of:")
    for topping in toppings:
        print(topping)


sandwich_orders('jam', 'lettuce', 'onions')
sandwich_orders('mayo', 'cheese')
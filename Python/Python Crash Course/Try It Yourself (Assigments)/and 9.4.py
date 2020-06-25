# 9.1 Restaurant


class Restaurant():
    """my first class"""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize attributes to describe a restaurant"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """this method print the two main arguments in init."""
        my_restaurant = "\nThe restaurant name is " + self.name.title() + "."
        restaurant_type = "\nIt serves " + self.type + " food."
        print(my_restaurant)
        print(restaurant_type)

    def open_restaurant(self):
        """this print a message indicating that the restaurant is open"""
        open = self.name.title() + " is now open."
        print(open)

    def set_number_served(self):
        """this shows the number of customers that has been served."""
        print("\nToday we have served " + str(self.number_served) + " customers.")

    def increment_number_served(self, customers_served):
        """this set the customer 'number_served' the given value"""
        self.number_served = customers_served


restaurant = Restaurant('condorito', 'junk food')
# restaurant is an instance of the Restaurant class

print(restaurant.name.title(), restaurant.type)

restaurant.describe_restaurant()

restaurant.open_restaurant()

print(restaurant.number_served)

restaurant.increment_number_served(29)

restaurant.set_number_served()
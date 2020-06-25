# 9.10

from restaurant_class import Restaurant


class IceCreamStand(Restaurant):
    """this is a child class from Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes from the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def displaying_flavors(self):
        """this method shows the available flavors."""
        print("\nWe have the following flavors:")
        for i in self.flavors:
            print(i.title())


restaurant = Restaurant('condorito', 'junk food')
# restaurant is an instance of the Restaurant class

print(restaurant.name.title(), restaurant.type)

restaurant.describe_restaurant()

restaurant.open_restaurant()

print(restaurant.number_served)

restaurant.increment_number_served(29)

restaurant.set_number_served()

print("...............................")

icecream_shop = IceCreamStand('sweet ice', 'icecream')

print(icecream_shop.name.title(), icecream_shop.type)

icecream_shop.describe_restaurant()

icecream_shop.displaying_flavors()

print('..............................................')

maca = Restaurant('macaroni', 'italian')

maca.describe_restaurant()
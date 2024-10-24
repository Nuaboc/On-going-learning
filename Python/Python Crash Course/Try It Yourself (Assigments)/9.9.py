# exercise from electric_car.py


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, brand, model, year):
        """initialize attributes to make a car."""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """this shows the main attributes of the instance."""
        long_name = str(self.year) + " " + self.brand + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """this shows the miles in the motor."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """this method updates the odometer counting."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """this increments miles."""
        self.odometer_reading += miles


class Battery() :
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describre_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """this method check the battery size and can change the capacity to 85. using =, not +=."""
        if self.battery_size < 85:
            self.battery_size = 85
        else:
            self.battery_size = self.battery_size


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, brand, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(brand, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("tesla", 'x', 2015)
print(my_tesla.get_descriptive_name())

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

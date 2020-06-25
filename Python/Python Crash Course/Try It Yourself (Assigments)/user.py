# 9.11 import Admin


class User:
    """details about users"""

    def __init__(self, first_name, last_name, age, birth_place):
        """initialize attributes to describe a user info"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birth_place = birth_place
        self.login_attempts = 0

    def describe_user(self):
        """obviously this describe the user name and last name."""
        user_info = self.first_name.title() + " " + self.last_name.title() + " has " + self.age + " years old."
        user_info2 = "\nFrom " + self.birth_place.title() + "."
        if self.birth_place:
            print(user_info, user_info2)
        elif self.birth_place == "":
            print(user_info)

    def greet_user(self):
        """this is obvious too"""
        greetings = "Hello " + self.first_name.title() + "."
        print(greetings)

    def increment_login_attempts(self, login_tries=1):
        """this increment the login attempts of the user by 1 (BY USING DEFAULT VALUE!!!!!)"""
        self.login_attempts += login_tries

    def reset_login_attempts(self):
        """this resets the login counts"""
        self.login_attempts = 0



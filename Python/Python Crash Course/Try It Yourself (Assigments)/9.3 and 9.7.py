
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


class Privileges():
    """this is a separate class for the privileges of an administrator"""

    def __init__(self):
        self.privileges = ["add posts", "delete posts", "ban users", "kick your ass"]

    def show_privileges(self):
        """this method shows the privileges of an administrator."""
        for show in self.privileges:
            print("Only the administrator can " + show + ".")


class Admin(User):
    """this is a sub-class of User."""

    def __init__(self, first_name, last_name, age, birth_place=""):
        """this initialize the Admin sub-class"""
        super().__init__(first_name, last_name, age, birth_place)
        self.privileges = Privileges()




user2 = User('ramon', 'betances', '49', 'ponce')

user2.describe_user()

user2.greet_user()

print('............................................')
# testing login attempts

print(user2.login_attempts)
user2.login_attempts = 4
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)

print('............................................')

admin = Admin("juan carlos", "gonzalez", str(32))

admin.describe_user()

admin.privileges.show_privileges()
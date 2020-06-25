
from user import User


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

# 9.7 and 9.8

from

user2 = User('ramon', 'betances', '49', 'ponce')
user2.describe_user()

user2.greet_user()

print('............................................')
# testing login attempts...

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
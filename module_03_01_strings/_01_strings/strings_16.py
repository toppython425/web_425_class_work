import string
import random

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)

# user_login = "".join(random.sample(string.ascii_lowercase, 6))
# user_password = "".join(random.sample((string.ascii_letters + string.digits), 8))
#
# print("login:", user_login)
# print("password:", user_password)
#
# symbols_list = []
#
# for i in range(500):
#     symbols_list.append(random.choice(string.ascii_lowercase))
#
# print(''.join(symbols_list))

my_string = "Мы рады\n встречать\n\n старых друзей."
print(my_string)
print()
print(string.capwords(my_string))

new_string = string.capwords(my_string)
print(string.capwords(new_string, sep='а'))
print(string.capwords(my_string, sep='а'))

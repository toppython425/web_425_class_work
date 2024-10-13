my_string = "Hello world! Hello python!"
print(my_string.startswith("H"))
print(my_string.startswith("Hello"))
print(my_string.endswith("!"))
print(my_string.endswith("python!"))

print(my_string.startswith('world', 6, 11))
print(my_string.startswith('world', 6))

print(my_string.endswith("Hello", 13, 18))

print(my_string.startswith("Hello", 6, 11))
print(my_string.startswith("world", 13, 18))


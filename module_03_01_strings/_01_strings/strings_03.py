# my_string = "Hello World!"
#
# string_slice = my_string[0:5]
# print(string_slice)
#
# string_slice = my_string[:5]
# print(string_slice)
#
# string_slice = my_string[6:11]
# print(string_slice)
#
# string_slice = my_string[6:]
# print(string_slice)


# my_string = "Hello World!"
# string_slice = my_string[-6:]
# print(string_slice)
#
# my_string = "Hello World!"
# string_slice = my_string[-7:]
# print(string_slice)
#
# my_string = "Hello World!"
# string_slice = my_string[-6:-3]
# print(string_slice)
#
# my_string = "Hello World!"
# string_slice = my_string[-6:11]
# print(string_slice)

my_string = "Hello World!"
string_step_slice = my_string[6:11:2]
print(string_step_slice)

my_string = "Hello World!"
string_step_slice = my_string[3::2]
print(string_step_slice)

my_string = "Hello World!"
string_step_slice = my_string[:8:2]
print(string_step_slice)

my_string = "Hello World!"
string_step_slice = my_string[::2]
print(string_step_slice)

my_string = "Hello World!"
string_step_slice = my_string[::-1]
print(string_step_slice)

my_string = "Hello World!"
string_step_slice = my_string[::-2]
print(string_step_slice)
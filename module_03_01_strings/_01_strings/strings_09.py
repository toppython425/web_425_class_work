# my_str = "Hello World!"
# center_string = my_str.center(20)
# print(center_string)
#
# center_string = my_str.center(20, "*")
# print(center_string)
#
# center_string = my_str.center(3, "*")
# print(center_string)
#
#
# left_string = my_str.ljust(20)
# print(left_string)
#
# left_string_stars = my_str.ljust(20, "*")
# print(left_string_stars)
#
# left_string_stars = my_str.ljust(3, "*")
# print(left_string_stars)
#
#
# right_string = my_str.rjust(20)
# print(right_string)
#
# right_string_stars = my_str.rjust(20, "*")
# print(right_string_stars)
#
# right_string_stars = my_str.rjust(3, "*")
# print(right_string_stars)

# my_str = "Hello World!\n\t\tHello Python!"
# print(my_str)
#
# my_str_expand = my_str.expandtabs()
# print(my_str_expand)
#
# my_str_expand = my_str.expandtabs(tabsize=10)
# print(my_str_expand)


# my_string = "****Hello World!****"
# print(my_string.strip('*'))
# print(my_string.rstrip('*'))
# print(my_string.lstrip('*'))
#
# with open('strip_file.txt', 'rt', encoding='utf-8') as file:
#     file_data = file.readlines()
#     for line in range(len(file_data)):
#         file_data[line] = file_data[line].strip()
#
#     print(file_data)


my_nums_string = "12345"
print(my_nums_string.zfill(10))


my_nums_string = "+12345"
print(my_nums_string.zfill(10))

my_nums_string = "-12345"
print(my_nums_string.zfill(10))

my_nums_string = "*12345"
print(my_nums_string.zfill(10))

my_nums_string = "/12345"
print(my_nums_string.zfill(10))

my_nums_string = "ab12345"
print(my_nums_string.zfill(10))

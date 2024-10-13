# import random
#
# nums_list = []
#
# for i in range(10):
#     nums_list.append(random.randint(-50, 50))
#
# print(nums_list)


my_string = input("Введите строку")
letters_count = 0
numbers_count = 0
space_count = 0

for symbol in my_string:
    if symbol.isdigit():
        numbers_count += 1
    elif symbol.isalpha():
        letters_count += 1
    elif symbol.isspace():
        space_count += 1

print(letters_count)
print(numbers_count)
print(space_count)
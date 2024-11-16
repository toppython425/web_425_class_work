# my_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}
# my_dict_keys = my_dict.keys()
# my_dict_values = my_dict.values()
#
# print(my_dict)
# print(my_dict_keys)
# print(my_dict_values)
# print(type(my_dict_keys))
# print(type(my_dict_values))
#
# print(list(my_dict_keys))
# print(list(my_dict_values))
#
# keys_list = [key for key in my_dict]
# print(keys_list)

my_dict = {'Cat': 'Кошка', 'Dog': 'Собака', 'Bird': 'Птица'}

for key in my_dict:
    print(key)
print()

for key in my_dict.keys():
    print(key)
print()

for value in my_dict.values():
    print(value)
print()

dict_keys = []
dict_values = []

for key, value in my_dict.items():
    print(f'Это ключ: {key}')
    print(f'Это значение: {value}')
    dict_keys.append(key)
    dict_values.append(value)

print(dict_keys)
print(dict_values)

print(my_dict.items())
print(type(my_dict.items()))

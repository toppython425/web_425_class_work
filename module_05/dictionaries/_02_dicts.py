# my_dict = {'cat': 'Котейка'}
# my_dict['dog'] = 'Собачка'
# print(my_dict)
# print()
#
# my_dict['cat'] = 'Кошка'
# my_dict['dog'] = 'Собака'
# print(my_dict)
# print()
#
# del my_dict['cat']
# print(my_dict)

my_dict = {'cat': 'Кошка', 'dog': 'Собака'}
shop_dict = {'parrot': 'Попугай', 'snake': 'Змея'}

my_dict.update(shop_dict)
print(my_dict)

my_dict = {'cat': 'Кошка', 'dog': 'Собака'}
shop_dict = {'parrot': 'Попугай', 'dog': 'Змея'}

my_dict.update(shop_dict)
print(my_dict)

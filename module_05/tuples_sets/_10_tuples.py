animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog', 'Cat', 'Turtle')
animals_list = list(animals_tuple)
print(f'Кортеж {animals_tuple}')
print(f'Список {animals_list}')

animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog', 'Cat', 'Turtle')
animals_string = ' : '.join(animals_tuple)
print(animals_string)

animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog', 'Cat', 'Turtle')
animals_set = set(animals_tuple)
print(animals_set)

animals_tuple_1 = (('Cat', 'Кот'), ('Dog', 'Собака'), ('Owl', 'Сова'))  # также работает и со вложенными списками
animals_dict = dict(animals_tuple_1)
print(animals_dict)

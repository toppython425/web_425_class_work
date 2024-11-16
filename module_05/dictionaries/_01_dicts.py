my_dict = {}
my_dict_1 = dict()

my_dict_2 = {'Петр': 201, 'Мария': 201}
my_dict_3 = {'Петр': 'Имя', 'Мария': ['фамилия', 'телефон'], 'Python': 'Язык программирования'}

my_dict_4 = dict(Петр='Имя', Python='Язык программирования')
my_dict_5 = dict((('Петр', ['фамилия', 'телефон']), ('Python', 'Язык программирования')))
print(my_dict_5)

print(my_dict_4['Python'])
print(my_dict_5['Петр'][0])

explations = {True: "Да все верно!", False: "Это не верно!"}

print(explations[3 > 2])
print(explations[3 < 2])

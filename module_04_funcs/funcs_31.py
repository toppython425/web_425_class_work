class MyHuman:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def set_name(self, user_rights, name):
        if user_rights in ['Admin', 'RequestUser']:
            self.__name = name
            return "Имя успешно изменено"
        else:
            return "Forbidden!!!"


me = MyHuman('Дмитрий', 'Сульжиц')
# print(me.__name)
# print(me.__surname)

me.__name = "Сергей"
# print(me.__name)
# print(me.__surname)
print(me.get_name())
print(me.get_surname())

print(me.set_name('RequestUser', 'Вася'))
print(me.get_name())

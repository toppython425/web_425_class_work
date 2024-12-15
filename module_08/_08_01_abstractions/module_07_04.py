class CakeForm:

    def __init__(self, dough, form, *args):
        self.dough = dough
        self.form = form
        if not args:
            self.ingredient_list = []
        else:
            self.ingredient_list = list(args)

    def make_dough(self):
        return f'Мы замешиваем тесто {self.dough}!'

    def make_form(self):
        return f'Мы выкладываем тесто в форму {self.form}'

    def add_ingredient(self, ingredient):
        self.ingredient_list.append(ingredient)
        return f"Добавлен {ingredient}"

    def add_ingredients(self, *args):
        list_ingredients = list(args)
        self.ingredient_list.extend(list_ingredients)
        return f"Добавлены {', '.join(list_ingredients)}"

    def cook_cake(self, time=40):
        if self.ingredient_list:
            if time > 80:
                return f'За {time} минут кекс из теста: {self.dough} форма: {self.form} с: {', '.join(self.ingredient_list)} сгорит!'
            return f'Мы выпекаем кекс из теста: {self.dough} форма: {self.form} с: {', '.join(self.ingredient_list)} {time} минут'
        else:
            if time > 80:
                return f'За {time} минут кекс из теста: {self.dough} форма: {self.form} сгорит!'
            return f'Мы выпекаем кекс из теста: {self.dough} форма: {self.form} {time} минут'


cake_1 = CakeForm('мучное', 'круглая', 'ром', 'марципан')
print(cake_1.make_dough())
print(cake_1.make_form())
print(cake_1.add_ingredient('изюм'))
print(cake_1.add_ingredients('курага', 'чернослив'))
print(cake_1.cook_cake())
print()
print(cake_1.cook_cake(100))

# print(cake_1.make_dough())
# print(cake_1.make_form())
# print(cake_1.cook_cake())
# print()
# print(cake_2.make_dough())
# print(cake_2.make_form())
# print(cake_2.cook_cake(100))

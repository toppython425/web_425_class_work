from module_08._08_02_OOPParadigms.module_08_12_13_main.classes.module_08_12 import Publication, Book, Magazine, Comix
from module_08._08_02_OOPParadigms.module_08_12_13_main.classes.module_08_13 import Car

publication = Publication("Все о слонах", "Группа слоноведов", "2021")
book = Book("Дубровский", "А.С. Пушкин", "2015", "23-015")
magazine = Magazine("Вокруг света", "Коллектив авторов", "2019", "№05-19")
comix = Comix("Человек Паук", "Стэн Ли", "1988", "№05-88")

car = Car("Volkswagen", "Caddy", "2017")

publication.display()
print()
book.display()
print()
magazine.display()
print()
comix.display()
print()

print(car.display())

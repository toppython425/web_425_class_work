class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @title.setter
    def title(self, title):
        self.__title = title
        print(f"Название книги изменено на {title}")

    @author.setter
    def author(self, title):
        self.__author = title
        print(f"Название книги изменено на {title}")


book = Book("Дубровский", "А.С. Пушкин")
print(book.title)
print(book.author)

book.__title = "Странный человек"
book.__author = 'М.Ю. Лермонтов'

print(book.title)
print(book.author)
print()

book.title = "Странный человек"
book.author = 'М.Ю. Лермонтов'
print(book.title)
print(book.author)

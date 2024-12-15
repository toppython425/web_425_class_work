class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Дубровский", "А.С. Пушкин")
print(book.title)
print(book.author)

book.title = 'Странный Человек'
book.author = 'М.Ю. Лермонтов'
print(book.title)
print(book.author)
print()


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author


book = Book("Дубровский", "А.С. Пушкин")
print(book._title)
print(book._author)

book._title = 'Странный Человек'
book._author = 'М.Ю. Лермонтов'
print(book._title)
print(book._author)
print()


class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title, access='user'):
        if access == 'moderator':
            self.__title = title
            return f"Название книги изменено на {title}"
        return "У вас нет необходимых прав доступа!"

    def set_author(self, title, access='user'):
        if access == 'moderator':
            self.__author = title
            return f"Название книги изменено на {title}"
        return "У вас нет необходимых прав доступа!"


book = Book("Дубровский", "А.С. Пушкин")
print(book.get_title())
print(book.get_author())

book.__title = "Странный человек"
book.__author = 'М.Ю. Лермонтов'

print(book.get_title())
print(book.get_author())
print()

print(book.set_title("Странный человек", 'user'))
print(book.set_author('М.Ю. Лермонтов', 'user'))
print(book.set_title("Странный человек", 'moderator'))
print(book.set_author('М.Ю. Лермонтов', 'moderator'))
print(book.get_title())
print(book.get_author())

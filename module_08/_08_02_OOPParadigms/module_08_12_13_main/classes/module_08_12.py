class Publication:

    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def display(self):
        print(f'Название: {self.__title}')
        print(f'Автор: {self.__author}')
        print(f'Год: {self.__year}')

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year


class Book(Publication):

    def __init__(self, title, author, year, code):
        super().__init__(title, author, year)
        self.__code = code

    def display(self):
        super().display()
        print(f'Код книги {self.__code}')

    def get_code(self):
        return self.__code


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.__issue_number = issue_number

    def display(self):
        super().display()
        print(f'Номер выпуска {self.__issue_number}')

    def get_issue_number(self):
        return self.__issue_number


class Comix(Magazine):

    def give_to_rent(self, days):
        return f'{self.get_title()}, автора {self.get_author()}, выдан на {days} дней'

    def give_to_rent_1(self, days):
        super().display()
        print(f'Выдан на {days} дней')

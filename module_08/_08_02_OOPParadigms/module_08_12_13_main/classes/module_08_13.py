class Car:

    def __init__(self, name, model, year):
        self.__name = name
        self.__model = model
        self.__year = year

    def display(self):
        return f'Мы протерли стекло на автомобиле {self.get_name()}'

    def get_name(self):
        return self.__name

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

class Classy:
    """Класс для примера"""
    varia = 1

    def __init__(self):
        self.var = 2

    def method(self):
        """Метод для примера"""
        pass

    def __hidden(self):
        pass


classy_object = Classy()
print(classy_object.__dict__)
print(Classy.__dict__)
print(Classy.__doc__)
print(classy_object.__doc__)

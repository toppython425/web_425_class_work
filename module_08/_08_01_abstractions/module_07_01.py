class Car:

    def __init__(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def go_to_a_ride(self, place, mileage):
        self.mileage += mileage
        return f'Мы поехали: {place}, расстояние {mileage}'


car_1 = Car(100000)
print(car_1.get_mileage())
print(car_1.go_to_a_ride('Дача', 40))
print(car_1.get_mileage())
print(car_1.go_to_a_ride('Брест', 700))
print(car_1.get_mileage())
print()

car_2 = Car(200000)
print(car_2.get_mileage())
print(car_2.go_to_a_ride('Деревню', 210))
print(car_2.get_mileage())
print(car_2.go_to_a_ride('Витебск', 500))
print(car_2.get_mileage())
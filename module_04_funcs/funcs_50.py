def my_space_address_mix(name: str, age=35, city=None, *args, **kwargs):
    print(name)
    print(age)
    if city:
        print(city)
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(key, value)


my_space_address_mix("Дмитрий", 36, "Минск", "Беларусь", "Восточная Европа", planet="Земля", star="Солнце")
print()
my_space_address_mix("Дмитрий", planet="Земля", star="Солнце")

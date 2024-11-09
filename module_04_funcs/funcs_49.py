def my_space_address(*args, **kwargs):
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(key, value)


my_space_address("Дмитрий", 36, planet="Земля", star="Солнце")

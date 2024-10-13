# my_nums_string = "0123456789"
# print(my_nums_string)
# print(type(my_nums_string))
#
# my_nums_int = int(my_nums_string)
# print(my_nums_int)
# print(type(my_nums_int))
#
# my_nums_float = float(my_nums_string)
# print(my_nums_float)
# print(type(my_nums_float))


leg_a = float(input("Введите длину 1го катета"))
leg_b = float(input("Введите длину 2го катета"))

print("Длина гипотенузы: " + str(round(((leg_a ** 2 + leg_b ** 2) ** 0.5), 2)))

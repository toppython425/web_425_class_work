# weather = input("Введите погоду хорошая-1/плохая-2: ")
#
# if weather == "1":
#     print("Идем гулять")
#     print("Получим удовольствие от прогулки")
# else:
#     print("Идем в кино!")
#     print("Купим попкорн")
#     print("Насладимся фильмом")
#
# print("Покушаем")


# weather = input("Введите погоду хорошая-1/плохая-2: ")
#
# if weather == "1":
#     print("Идем гулять")
#     print("Получим удовольствие от прогулки")
#     nice_restaurant = input("Нашли хороший ресторанчик? 1-Да, 2-Нет: ")
#     if nice_restaurant == "1":
#         print("Съедим стейк!")
#     else:
#         print("Съедим что найдем")
# else:
#     print("Идем в кино!")
#     print("Купим попкорн")
#     print("Насладимся фильмом")
#     print("Покушаем")


# weather = input("Введите погоду солнечная - 1/пасмурная - 2:")
# tickets = input("Билет: да - 1/ нет - 2: ")
# table = input("Cтолик: да - 1/нет - 2: ")
#
# if weather == '1':
#     print("Идем гулять!")
# elif tickets == '1':
#     print('Идем в кино!')
# elif table == '1':
#     print("Кушаем стейк, в ресторане!")
# else:
#     print("Закажем пиццу")
#     print("Будем играть в настолки дома")
#
# print("В общем хорошо проведем время!")

weather = input("Введите погоду солнечная - 1/пасмурная - 2/для ресторана - 3:")
# tickets = input("Билет: да - 1/ нет - 2: ")
# table = input("Cтолик: да - 1/нет - 2: ")

if weather == '1':
    print("Идем гулять!")

elif weather == '2':
    print('Идем в кино!')

elif weather == '3':
    print("Кушаем стейк, в ресторане!")

else:
    print("Закажем пиццу")
    print("Будем играть в настолки дома")


print("В общем хорошо проведем время!")
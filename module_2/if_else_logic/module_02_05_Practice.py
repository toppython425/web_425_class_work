# num_1 = int(input())
# num_2 = int(input())
#
# print(num_1 == num_2)

# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# if num_2 > num_1:
#     num_1 = num_2
# if num_3 > num_1:
#     num_1 = num_3
#
# print(num_1)


# account_sum = float(input("Сумма: "))
#
# if account_sum >= 500:
#     print("Средств достаточно")
# else:
#     print("Средств НЕдостаточно")


# humidity = round(float(input("Введите влажность воздуха: ")), 2)
#
# # if 30 <= humidity <= 60:
# if 29.99 < humidity < 60.01:
#     print("Влажность комфортная")
# else:
#     print("Обратите внимание на влажность")


# temperature = round(float(input("Введите температуру воздуха: ")), 1)
#
# if temperature < 36.5:
#     print("Температура понижена")
# elif 36.5 <= temperature <= 36.7:
#     print("Температура в норме!")
# elif temperature > 36.7:
#     print("Температура повышена")
# else:
#    print("Температура повышена")




stars = input("Введите количество звездочек: ")

if stars == "*":
    print("Ужасно")
elif stars == "**":
    print("Очень плохо")
elif stars == "***":
    print("Средненько")
elif stars == "****":
    print("Всё в порядке")
elif stars == "*****":
    print("Прекрасная поездка!")
else:
    print("Некорректный ввод")


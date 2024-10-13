# car_speed = 100
# if car_speed > 50:
#     print("Автомобиль едет быстрее 50 км/ч")

# car_speed = 150
# motorcycle_speed = 100
# if car_speed > motorcycle_speed:
#     print("Автомобиль быстрее мотоцикла!")
# else:
#     print("Мотоцикл быстрее автомобиля!")
#
# car_speed = 100
# motorcycle_speed = 100
# if car_speed > motorcycle_speed:
#     print("Автомобиль быстрее мотоцикла!")
# if motorcycle_speed > car_speed:
#     print("Мотоцикл быстрее автомобиля!")
# else:
#     print("Скорости равны")


# car_speed = 130
# motorcycle_speed = 100
# if car_speed > motorcycle_speed:
#     print("Автомобиль быстрее мотоцикла!")
#     motorcycle_speed += 50
# elif motorcycle_speed > car_speed:
#     print("Мотоцикл быстрее автомобиля!")
# else:
#     print("Скорости равны")


# user_input = int(input("Выберете ваш ответ: "))
#
# if user_input == 1:
#     print("Выбран Вариант A")
# else:
#     if user_input == 2:
#         print("Выбран Вариант B")
#     else:
#         if user_input == 3:
#             print("Выбран Вариант C")
#         else:
#             if user_input == 4:
#                 print("Выбран Вариант D")
#             else:
#                 print("Нет таких вариантов")


# user_input = int(input("Выберете ваш ответ: "))
#
# if user_input == 1:
#     print("Выбран Вариант A")
# elif user_input == 2:
#     print("Выбран Вариант B")
# elif user_input == 3:
#     print("Выбран Вариант C")
# elif user_input == 4:
#     print("Выбран Вариант D")
# else:
#     print("Нет таких вариантов")


account = int(input("Введите сумму пополнения"))
account = abs(account)

if account > 0:
    withdrawal = int(input("Введите сколько вы хотите снять"))
    withdrawal = abs(withdrawal)
    if withdrawal <= account:
        account -= withdrawal
        print(f"Вот ваша сумма {withdrawal}")
        print(f"У вас осталось {account}")
    else:
        print(f"На счете только {account}")
else:
    print("В копилке денег нет")

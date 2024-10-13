# start = 1
# finish = 10
# step = 2
#
# for i in range(start, finish, step):
#     print(f"Значение i = {i}")
#
# print()
#
# start = 10
# finish = 0
# step = -2
#
# for i in range(start, finish, step):
#     print(f"Значение i = {i}")

num = int(input("Введите число: "))
start = int(input("С какой степени начнем: "))
finish = int(input("По какую степень возводить: "))

for exp in range(start, finish + 1):
    result = num ** exp
    print(f'{num} в степени {exp}, равно: {result}')

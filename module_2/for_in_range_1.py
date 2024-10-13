# number = 0
# for i in range(10):
#     number = number + 1
#     if number == 3:
#         break
#     print(f'Number is {str(number)}')
#
# print("Out of loop")


# number = 0
# for i in range(10):
#     number = number + 1
#     if number == 5 or number == 7:
#         continue
#     print(f'Number is {str(number)}')
#
# print("Out of loop")

# number = 0
# for i in range(10):
#     number = number + 1
#     if number == 5 or number == 7:
#         pass
#     print(f'Number is {str(number)}')
#
# print("Out of loop")


# number = 0
# for i in range(10):
#     number = number + 1
#     if number == 12:
#         break
#     print(f'Number is {str(number)}')
# else:
#     print("Цикл закончился без прерываний.")
#
# print("Out of loop")
#
# x = int(input("Введите значение х: "))
# y = int(input("Введите значение y: "))
# if x % 2 == 0:
#     for i in range(x, y + 1, 2):
#         print(f"крутим цикл {i}")
# else:
#     for i in range(x + 1, y + 1, 2):
#         print(f"крутим цикл {i}")


# user_num = int(input("Введите ваше число."))
# number = 1
#
# for i in range(1, user_num + 1):
#     number *= i
#
# print(number)
line_len = int(input("Введите длину линии: "))
symbol = input("Введите символ: ")
my_str = ''

for i in range(line_len):
    my_str += symbol

print(my_str)
try:
    print("основной код")
    num = int(input("Введите число: "))
except BaseException:
    print("Код если возникло исключение!")
else:
    print(num * 2)
finally:
    print("Программа завершила работу.")

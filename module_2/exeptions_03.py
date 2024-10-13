from exceptions_04_custom import OnlyPositiveException

try:
    apples = int(input("Введите количество яблок которые у вас есть: "))
    if apples < 0:
        raise OnlyPositiveException
except OnlyPositiveException:
    print("У вас не может быть отрицательное количество яблок!!!")
else:
    print(f"У вас {apples} яблок!")

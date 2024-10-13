from exceptions_04_custom import OnlyPositiveException

try:
    amount = int(input("Введите количество полученных предметов: "))
    if amount < 0:
        raise OnlyPositiveException("У вас не может быть отрицательное количество предметов!!")
    items_type = input("Укажите тип полученных предметов: ")
    parts_quantity = int(input("Введите количество частей: "))
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except (ZeroDivisionError, ValueError):
    print("Получено некорректное значение!")
except OnlyPositiveException as ex:
    print(ex)
except:
    print("Что-то пошло не так!")
else:
    print(f"Поставка из {amount}, {items_type} сохранена.")
    if amount_1_part_rest == 0:
        print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
    else:
        print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
        print(f"Не распределенный остаток состоит из {amount_1_part_rest} {items_type}")
finally:
    print("Программа-распределитель завершила свою работу!")

try:
    amount = int(input("Введите количество полученных предметов: "))
    items_type = input("Укажите тип полученных предметов: ")
    parts_quantity = int(input("Введите количество частей: "))
    amount_1_part = amount // parts_quantity
    amount_1_part_rest = amount % parts_quantity
except ValueError:
    print("Количество должно быть числом int")
except ZeroDivisionError:
    print("Невозможно разделить поставку на 0 частей")
else:
    print(f"Поставка из {amount}, {items_type} сохранена.")
    if amount_1_part_rest == 0:
        print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
    else:
        print(f"Каждая из {parts_quantity} частей состоит из {amount_1_part} {items_type}")
        print(f"Не распределенный остаток состоит из {amount_1_part_rest} {items_type}")
finally:
    print("Программа-распределитель завершила свою работу!")

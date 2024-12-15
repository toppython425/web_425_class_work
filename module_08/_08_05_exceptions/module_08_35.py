class MyZeroDivision(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivision("Очень плохие новости!")
    else:
        raise ZeroDivisionError("Плохие новости!")


for mode in [True, False]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print("Деление на ноль!")


for mode in [True, False]:
    try:
        do_the_division(mode)
    except MyZeroDivision as mZD:
        print(mZD)
    except ZeroDivisionError as ZD:
        print("Деление на ноль!")

try:
    x = 1 / 0
except Exception as ex:
    print(ex)


try:
    raise ValueError
except BaseException as ex:
    print(type(ex).__name__)


raise ValueError("Вы сделали ошибку при введении значения.")
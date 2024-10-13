try:
    raise Exception
except Exception:
    print("Что-то пошло не так")
except ValueError:
    print("Получено нужное исключение ValueError")

try:
    raise ValueError
except Exception:
    print("Что-то пошло не так")
except ValueError:
    print("Получено нужное исключение ValueError")

try:
    raise ValueError
except ValueError:
    print("Получено нужное исключение ValueError")
except Exception:
    print("Что-то пошло не так")

try:
    raise Exception
except ValueError:
    print("Получено нужное исключение ValueError")
except Exception:
    print("Получено нужное исключение Exception")

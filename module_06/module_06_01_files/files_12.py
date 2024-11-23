import os

# base_dir = r'test_path_2/test_2.txt'
# new_dir = r'test_path_1/test_2_new_place.txt'
#
# try:
#     os.rename(base_dir, new_dir)
# except FileNotFoundError:
#     print("Файл не найден!")
# except FileExistsError:
#     print('Такой файл уже существует!')
# else:
#     print(f"Файл успешно перемещен, новое расположение файла\n{os.path.abspath(new_dir)}")
# finally:
#     print("Программа завершила свою работу!")


base_dir = r'test_path_1/shopping_new_place.txt'
new_dir = r'test_path_2/shopping.txt'

try:
    os.renames(base_dir, new_dir)
except FileNotFoundError:
    print("Файл не найден!")
except FileExistsError:
    print('Такой файл уже существует!')
else:
    print(f"Файл успешно перемещен, новое расположение файла\n{os.path.abspath(new_dir)}")
finally:
    print("Программа завершила свою работу!")


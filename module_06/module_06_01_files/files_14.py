import os
import shutil

# my_path = 'test_path_1/guests.txt'
# try:
#     os.remove('test_path_1/guests.txt')
# except FileNotFoundError:
#     print('Файл не найден')
# else:
#     print("Файл был успешно удален!")


try:
    shutil.rmtree('test_path_1')
except FileNotFoundError:
    print('Директория не найдена!')
else:
    print("Директория была успешно удалена!")


import os


file_path = 'test_path_2/shopping.txt'

print(os.path.getctime(file_path))
print(os.path.getmtime(file_path))
print(os.path.getatime(file_path))
print(os.path.getsize(file_path))
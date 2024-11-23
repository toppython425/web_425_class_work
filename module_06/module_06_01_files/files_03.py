import os

base_dir = '..'
test_dir = 'test_path_1'

path_base_test_dir = os.path.join(base_dir, test_dir)
print(path_base_test_dir)

for path, dirnames, filenames in os.walk(path_base_test_dir):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')

new_dir = r'my_new_dir'
print()

path_dir_new_dir = os.path.join(base_dir, test_dir, new_dir)
print(path_dir_new_dir)
try:
    os.mkdir(path_dir_new_dir)
except FileExistsError:
    print(r"Невозможно создать файл, так как он уже существует")

for path, dirnames, filenames in os.walk(path_base_test_dir):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')
print()

os.rmdir(path_dir_new_dir)
for path, dirnames, filenames in os.walk(path_base_test_dir):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')

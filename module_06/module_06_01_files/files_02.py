import os

path_learning = r'/module_05'
print(os.path.isabs(path_learning))
print(os.path.isfile(path_learning))
print(os.path.isdir(path_learning))
print(os.path.islink(path_learning))
print()

path_learning_file = r'/module_06/module_06_01_files/files_01.py'
print(os.path.isabs(path_learning_file))
print(os.path.isfile(path_learning_file))
print(os.path.isdir(path_learning_file))
print(os.path.islink(path_learning_file))



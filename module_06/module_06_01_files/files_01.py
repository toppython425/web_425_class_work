import os

# path_learning = r'D:\work_Top_Academy_web\web_425_class_work\module_05'
#
# for path, dirnames, filenames in os.walk(path_learning):
#     print(f'path - {path}')
#     print(f'dirnames - {dirnames}')
#     print(f'filenames - {filenames}')

# disk = 'D:\\'
# dir_1 = 'work_Top_Academy_web'
# dir_2 = 'web_425_class_work'
# dir_3 = 'module_05'
#
# path_module_05 = os.path.join(disk, dir_1, dir_2, dir_3)
# print(path_module_05)
#
# for path, dirnames, filenames in os.walk(path_module_05):
#     print(f'path - {path}')
#     print(f'dirnames - {dirnames}')
#     print(f'filenames - {filenames}')

base_dir = '..'
test_dir = 'test_path_1'

path_base_test_dir = os.path.join(base_dir, test_dir)
print(path_base_test_dir)

for path, dirnames, filenames in os.walk(path_base_test_dir):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')
print()

print(os.path.abspath('files_01.py'))
my_abspath_dir = os.path.abspath('..')
my_abspath_current_file = os.path.abspath(__file__)

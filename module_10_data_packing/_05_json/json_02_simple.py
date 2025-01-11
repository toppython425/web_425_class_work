import json

from module_06.module_06_01_files.files_01 import path_base_test_dir


class MyCat:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


my_cat = MyCat('Франц', 3, 'Самец')
print(my_cat.__dict__)

json_data = json.dumps(my_cat.__dict__, default=lambda obj_cat: obj_cat.__dict__, ensure_ascii=False, indent=2)
print(json_data)

with open(r'json_files\my_cat.json', 'w', encoding='utf-8') as fh:
    json.dump(my_cat, fh,
              default=lambda obj_cat: obj_cat.__dict__,
              ensure_ascii=False, indent=2)

with open(r'json_files\my_cat.json', 'r', encoding='utf-8') as fh:
    python_cat = json.load(fh)
print(python_cat)
print(type(python_cat))
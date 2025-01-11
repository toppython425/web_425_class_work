import json

my_dict = {
    'my_string': 'some_string',
    'my_integer': 123,
    'my_tuple': (1, 2, 3, 4, 5),
    'my_bool': True,
    'my_none': None,
}

with open(r'json_files\my_data.json', 'w', encoding='utf-8') as fh:
    json.dump(my_dict, fh, ensure_ascii=False, indent=2)
    # my_json_string = json.dumps(my_dict)
    # fp.write(my_json_string)

with open(r'json_files\my_data.json') as fh:
    python_data = json.load(fh)
    # json_string = fp.read()
    # python_data = json.loads(json_string)

print(python_data)

my_json_string = json.dumps(my_dict)
print(my_json_string)
print(type(my_json_string))

my_dict_from_json_string = json.loads(my_json_string)
print(my_dict_from_json_string)
print(type(my_dict_from_json_string))

for key, value in my_dict_from_json_string.items():
    if 'tuple' in key:
        my_dict_from_json_string[key] = tuple(value)
print(my_dict_from_json_string)

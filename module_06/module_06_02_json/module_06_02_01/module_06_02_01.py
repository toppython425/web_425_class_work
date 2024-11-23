import json

python_data = {
    0: "Нулевой",
    1: 1234,
    2: ['item1', 'item2'],
    3: ('item1', 'item2'),
    4: None,
    5: True,
    6: False,
}


print(type(python_data))
json_data = json.dumps(python_data, ensure_ascii=False, indent=2)
print(json_data)
print(type(json_data))

with open('my_json.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
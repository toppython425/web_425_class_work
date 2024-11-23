import json

with open('my_json.json', encoding='utf-8') as file:
    json_data = file.read()
    print(type(json_data))
    python_data = json.loads(json_data)

print(python_data)
print(type(python_data))


with open('my_json.json', encoding='utf-8') as fp:
    python_data = json.load(fp)

print(python_data)
print(type(python_data))
def get_dict_data(filename):
    managers_dict = {}
    with open(filename, encoding='utf-8') as managers_data:
        for manager_data in managers_data:
            clean_data = manager_data.strip().split(':')
            manager = clean_data[0]
            company = clean_data[1]
            head_company = clean_data[2]
            managers_dict[(company, head_company)] = manager
    return managers_dict


managers_data_dict = get_dict_data('managers_data.txt')
print(managers_data_dict)

for companies, manager in managers_data_dict.items():
    print(f'{manager} работает в компании {companies[0]} которая принадлежит {companies[1]}')


def write_managers_data(filename, data_to_write):
    with open(f'{filename}.txt', 'w', encoding='utf-8') as managers_data:
        for companies, manager in data_to_write.items():
            managers_data.write(f'{manager}||{companies[0]}||{companies[1]}\n')
    print("Данные записаны!")
    return "Данные записаны!"


managers_to_write = {
    ('Bethesda', 'Microsoft'): 'Тодд Говард',
    ('ID Software', 'Microsoft'): 'Джон Кармак',
    ('AMD', 'AMD'): 'Лиза Су'
}

print(write_managers_data('managers_data_wrote', managers_to_write))

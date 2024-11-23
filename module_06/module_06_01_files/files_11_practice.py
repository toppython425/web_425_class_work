# str_list = ["Тодд Говард:Bethesda:Microsoft", "Джон Кармак:ID Software:Microsoft", "Лиза Су:AMD:AMD"]
#
# with open('output.txt', 'w', encoding="utf-8") as file:
#     for line in str_list:
#         file.write(line + '\n')
#         # file.write(f'{line}\n')
import re


with open('managers_data.txt', 'r', encoding='utf-8') as file:
    file_data = file.read()
    data_list = re.split(r'[,\n.]', file_data)

counter = 0
for data in data_list:
    counter += len(data)

print(counter)





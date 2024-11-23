# virus_code = 'print("Я вирус")'
#
# with open('files_09.py', 'a', encoding='utf-8') as file:
#     file.write(f"\n{virus_code}\n")
virus_code = 'print("Я вирус")'

with open('files_09.py', encoding='utf-8') as file:
    content = file.read()
    new_content = content.replace('print("Я вирус")', '')
    if virus_code in content:
        print("Вирус обнаружен!!!")
        with open('files_09.py', 'w', encoding='utf-8') as clean_file:
            clean_file.write(new_content)
    else:
        print("Вирусов нет!")


print(list("Вирусов нет!"))

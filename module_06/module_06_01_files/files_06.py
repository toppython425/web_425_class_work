# with open('write_data.txt', 'wt', encoding='utf-8') as file:
#     file.write('Hello ')
#     file.write('World\n')
#     file.write('Hello ')
#     file.write('Python\n')

with open('write_data.txt', 'at', encoding='utf-8') as file:
    file.write('Hello ')
    file.write('World\n')
    file.write('Hello ')
    file.write('Python\n\n')

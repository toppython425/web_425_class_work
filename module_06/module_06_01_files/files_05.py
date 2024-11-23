guests_count = 0
with open('guests.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip())
        guests_count += 1
print(f'Количество гостей: {guests_count}')
print()

with open('guests.txt', 'r', encoding='utf-8') as file:
    guests_list = file.readlines()
    print(guests_list)

guests_count = len(guests_list)
print(''.join(guests_list))
print(f'Количество гостей: {guests_count}')

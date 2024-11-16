guests = {
    "Сергей": 1600,
    "Андрей": 2200,
    "Дмитрий": 1800,
    "Диана": 2300,
    "Александр": 2500,
}

total = 0

guests_names = ', '.join(guests.keys())

for check_value in guests.values():
    total += check_value

print(f"В кафе были {guests_names}")
print(f"Общий чек {total}")
print(f"Каждый платит: {total / len(guests)}")

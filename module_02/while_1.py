odd_numbers = 0
even_numbers = 0

number = int(input("Введите число или 0, для остановки программы."))

# 0 прекращает цикл

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Введите число или 0, для остановки программы."))

print(f"Четные: {even_numbers}")
print(f"Нечетные: {odd_numbers}")

import random

random_number = random.randint(1, 500)
print(random_number)

counter = 1
user_number = int(input("Введите число: "))

for i in range(501):
    if user_number == 0:
        counter -= 1
        break
    elif user_number == random_number:
        break
    elif user_number < random_number:
        print("Загаданное число больше!")
    else:
        print("Загаданное число меньше!")
    counter += 1
    user_number = int(input("Введите число: "))

print(f"Всего попыток: {counter}")

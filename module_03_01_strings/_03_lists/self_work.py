full_name = input("Добрый день! Назовите ваше имя и фамилию: ").strip().title()
print(f"Приятно познакомится {full_name}, проверим ваши знания по зоологии:")

score = 0
correct_answers = 0
correct_answer_1 = "саванный слон"
correct_answer_2 = "белый медведь"
correct_answer_3 = "гепард"

user_answer_1 = input("1й вопрос - самое крупное наземное млекопитающее, с хоботом и большими ушами: ").strip().lower()
if user_answer_1 == correct_answer_1:
    score += 10
    correct_answers += 1
    print(f"Все верно это - {correct_answer_1}")
else:
    print(f"Неверно верный ответ - {correct_answer_1}")

user_answer_2 = input("2-й вопрос - самый крупный наземный хищник, обитает в Арктике: ").strip().lower()
if user_answer_2 == correct_answer_2:
    score += 10
    correct_answers += 1
    print(f"Все верно это - {correct_answer_2}")
else:
    print(f"Неверно верный ответ - {correct_answer_2}")

user_answer_3 = input(
    "3-й вопрос - самый быстрый наземный хищник, основная часть популяции приходится на страны Африки: ").strip().lower()
if user_answer_3 == correct_answer_3:
    score += 10
    correct_answers += 1
    print(f"Все верно это - {correct_answer_3}")
else:
    print(f"Неверно верный ответ - {correct_answer_3}")

user_percent = (correct_answers / 3) * 100
print(f'''Вот и все вы дали {correct_answers} верных ответов.
Вы получили {score} очков.
Это {round(user_percent, 2)} процентов верных ответов.''')


class OnlyIntException(Exception):
    def __init__(self):
        pass


user_start = ''
user_finish = ''

try:
    user_start = input("Введите начало таблицы умножения: ")
    user_finish = input("Введите окончание таблицы умножения: ")
    if '.' in user_start or '.' in user_finish:
        raise OnlyIntException
    user_start = int(user_start)
    user_finish = int(user_finish)
except OnlyIntException:
    print("Вы ввели не целое число!")
except ValueError:
    print("Вы ввели не число вовсе")
else:
    for i in range(user_start, user_finish + 1):
        for j in range(1, 11):
            print(f'{i} * {j} = {i * j}', end='\t')
        print()

while True:
    num_1 = int(input('Введите 1е число'))
    num_2 = int(input('Введите 2е число'))
    num_3 = int(input('Введите 3е число'))

    if 0 < num_1 < 21 and 0 < num_2 < 21 and 0 < num_3 < 21 and num_1 != num_2 != num_3:
        break
    else:
        print("Все 3 числа должны быть разные, а также больше 0 но меньше 21")

for i in range(1, 21):
    if i == num_1 or i == num_2 or i == num_3:
        continue
    print(i)

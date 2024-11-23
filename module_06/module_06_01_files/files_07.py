user_language = input("Какай язык вы учите? ")
user_time = input("Как долго? ")
user_institution = input("Где? ")

user_answers = [user_language, user_time, user_institution]

with open('write_user_data.txt', 'a', encoding='utf-8') as file:
    for answer in user_answers:
        file.write(f'{answer}\n')
    file.write(f'\n')
print("Ответы записаны!")

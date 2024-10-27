import random


def get_random_genre(category, categories_matrix):
    if category == 'кино':
        return random.choice(categories_matrix[0])
    elif category == 'книги':
        return random.choice(categories_matrix[1])
    elif category == 'игры':
        return random.choice(categories_matrix[2])
    else:
        return "Не знаю такой категории!!"


cinema_genres = ["Драма", "Комедия", "Фэнтези", "Ужасы"]
book_genres = ["Поэма", "Водевиль", "Роман", "Проза"]
game_genres = ["Симулятор", "Аркада", "RPG", "Инди"]
my_categories_matrix = [cinema_genres, book_genres, game_genres]

print(get_random_genre('кино', my_categories_matrix))
print(get_random_genre('книги', my_categories_matrix))
print(get_random_genre('игры', my_categories_matrix))


def random_genre_lists(category: str, cinema_genres: list, book_genres: list, game_genres: list):
    if category == "кино":
        return random.choice(cinema_genres)

    elif category == "книги":
        return random.choice(book_genres)

    elif category == "игры":
        return random.choice(game_genres)

    else:
        return "Не знаю такой категории!"


print(random_genre_lists('кино', cinema_genres, book_genres, game_genres))
print(random_genre_lists('книги', cinema_genres, book_genres, game_genres))
print(random_genre_lists('игры', cinema_genres, book_genres, game_genres))

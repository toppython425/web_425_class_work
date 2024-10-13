import random

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Horror"]
index = random.randint(0, len(cinema_genres) - 1)
genre = cinema_genres[index]
print(f'Ваш случайный жанр {genre}\n')

random.shuffle(cinema_genres)
genre = cinema_genres[0]
print(f'Ваш случайный жанр {genre}\n')

genre_list = random.sample(cinema_genres, 3)
print(f'Ваш случайные жанры: {', '.join(genre_list)}\n')

genre = random.choice(cinema_genres)
print(f'Ваш случайные жанры: {genre}\n')


import random

# cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Romance"]
# print(cinema_genres)
# random.shuffle(cinema_genres)
# print(cinema_genres)


# cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Romance"]
# genres_sample = random.sample(cinema_genres, 3)
# print(genres_sample)
#
# some_str = "Привет! Я строка"
# items = random.sample(some_str, len(some_str))
# print(items)
# result = ''.join(items)
# print(result)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Romance"]
random_genre = random.choice(cinema_genres)
print(random_genre)
some_str = "Привет! Я строка"
print(random.choice(some_str))
"""Поиск нескольких индексов"""

cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Romance"]
genre_to_find = "Comedy"

for i in range(len(cinema_genres)):
    if cinema_genres[i] == genre_to_find:
        print(i)

genre_index = 0

for genre in cinema_genres:
    if genre == genre_to_find:
        print(genre_index)
    genre_index += 1

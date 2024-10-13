cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
print("Drama" in cinema_genres)
print("Detective" in cinema_genres)
print("Drama" not in cinema_genres)
print("Detective" not in cinema_genres)

genre_to_find = "Drama"
if genre_to_find in cinema_genres:
    print(f"{genre_to_find} есть в списке жанров!")
else:
    print(f"Жанра {genre_to_find} нет в списке жанров:(")

genre_to_append = "Detective"
if genre_to_append not in cinema_genres:
    cinema_genres.append(genre_to_append)
    print(f"Жанр {genre_to_append} добавлен!")
else:
    print(f"Жанр {genre_to_append} уже есть в списке")

print(cinema_genres)

user_answer = input().strip().lower()
if user_answer in ['да', 'yes', 'y']:
    pass
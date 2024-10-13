cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres = cinema_genres.copy()

print(literature_genres is cinema_genres)
print(cinema_genres is literature_genres)

literature_genres.append('Scy-Fy')

print(f"Кино {cinema_genres}")
print(f"Литература {literature_genres}")

cinema_genres_1 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_1 = list(cinema_genres_1)

print(literature_genres_1 is cinema_genres_1)
print(cinema_genres_1 is literature_genres_1)

cinema_genres_2 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_2 = cinema_genres_2[:]

print(literature_genres_2 is cinema_genres_2)
print(cinema_genres_2 is literature_genres_2)


cinema_genres_3 = ["Drama", "Comedy", "Fantasy", "Romance"]
literature_genres_3 = []

for i in range(len(cinema_genres_3)):
    literature_genres_3.append(cinema_genres_3[i])

print(literature_genres_3 is cinema_genres_3)
print(cinema_genres_3 is literature_genres_3)





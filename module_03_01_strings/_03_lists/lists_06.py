# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance"]
# book_genres = ["Detective", "Poem", "Scy-Fy", "Fantasy"]

# for cinema_genre in cinema_genres:
#     print(cinema_genre)
#
#
# for index in range(len(cinema_genres)):
#     print(f"{index} {cinema_genres[index]}")
#     print(f"{index} {book_genres[index]}")


# cinema_genres.append("Action")
# print(cinema_genres)
#
# cinema_genres_1 = ["Drama", "Comedy", "Fantasy", "Romance"]
# genres_to_add = ["Action", "Detective"]
# cinema_genres_1.extend(genres_to_add)
# print(cinema_genres_1)
#
# cinema_genres_2 = ["Drama", "Comedy", "Fantasy", "Romance"]
# cinema_genres_2.insert(2, "Action")
# print(cinema_genres_2)

cinema_genres_3 = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
cinema_genres_4 = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
for cinema_genre in cinema_genres_4:
    if cinema_genre == "Comedy":
        cinema_genres_4.remove("Comedy")

print(cinema_genres_4)

print()

cinema_genres_pop = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
popped_item = cinema_genres_pop.pop(2)
print(popped_item)
print(cinema_genres_pop.pop(2))
print(cinema_genres_pop)

print()

cinema_genres_clear = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
cinema_genres_clear.clear()
print(cinema_genres_clear)

print()

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
item_index = cinema_genres.index("Comedy")
print(item_index)

print()

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
item_count = cinema_genres.count("Comedy")
print(item_count)


cinema_genres_sort = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
# cinema_genres_sort.sort()
# print(cinema_genres_sort)
# cinema_genres_sort.sort(reverse=True)
# print(cinema_genres_sort)
cinema_genres_sort.reverse()
print(cinema_genres_sort)

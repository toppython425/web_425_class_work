# animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog')
# print(len(animals_tuple))
#
# nums_tuple = (1, 2, 3, 4, 5.5)
# print(sum(nums_tuple))
#
# animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog')
# nums_tuple = (1, 2, 3, 4, 5.5)
#
# print(min(animals_tuple))
# print(min(nums_tuple))
# print(max(animals_tuple))
# print(max(nums_tuple))

animals_tuple = ('Cat', 'Turtle', 'Snake', 'Dog')
nums_tuple = (1, 2, 3, 4, 5.5)

sorted_tuple_animals = tuple(sorted(animals_tuple, reverse=True))
print(sorted_tuple_animals)

sorted_tuple_nums = tuple(sorted(nums_tuple, reverse=True))
print(sorted_tuple_nums)




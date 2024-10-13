# category = ["Drama", "Comedy", "Fantasy"]
# print(category)
#
# category[0] = "Драма"
# category[1] = "Комедия"
# category[2] = "Фэнтези"
#
# print(category)


category_list = ["Drama", "Comedy", "Алфавит", "Zantasy"]
nums_list = [3, 1, 2, 11, 25]
print(len(category_list), len(nums_list))
print(max(category_list), max(nums_list))
print(min(category_list), min(nums_list))
print(sum(nums_list))

sorted_list = sorted(category_list)
sorted_nums = sorted(nums_list)
print(sorted_list)
print(sorted_nums)

sorted_list_rev = sorted(category_list, reverse=True)
sorted_nums_rev = sorted(nums_list, reverse=True)
print(sorted_list_rev)
print(sorted_nums_rev)


example_list_nums = ['03', '1', '02', '11', '0100']
sorted_nums_rev = sorted(example_list_nums, reverse=True)
print(sorted_nums_rev)

example_list_symbols = ['*', '$', '#', '%', '@']
print(sorted(example_list_symbols))


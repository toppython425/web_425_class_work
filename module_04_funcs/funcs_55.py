# def print_list_data():
#     func_list = ["Боевик", "Комедия", "Драма"]
#     my_list.append("Проза")
#     print(func_list)
#     print(my_list)
#
#
# my_list = ["Новелла", "Роман", "Пьеса"]
# print_list_data()


def print_list_data_1(some_list):
    some_list.append("Проза")
    for item in some_list:
        print(item)


my_list = ["Новелла", "Роман", "Пьеса"]
print_list_data_1(my_list)

my_list = [x for x in range(6)]
print(my_list)
my_list_2 = list(map(lambda x: 2 ** x, my_list))
print(my_list_2)

my_gen = (x for x in range(5))
my_gen_2 = list(map(lambda x: 2 ** x, my_gen))
print(my_gen_2)


def my_func(x):
    return 2 ** x


result = list(map(my_func, my_list))
print(result)

for i in map(lambda x: 2 ** x, my_list):
    print(i, end=' ')

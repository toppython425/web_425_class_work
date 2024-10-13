my_list = [2 ** i for i in range(10)]
print(my_list)

my_list_1 = []
for i in range(10):
    my_list_1.append(2 ** i)
print(my_list_1)

print()

square_list = [i * i for i in range(11)]
print(square_list)

square_list_1 = []
for i in range(11):
    square_list_1.append(i * i)
print(square_list_1)

print()

list_from_str = [sym + "*" for sym in "my_string"]
print(list_from_str)

list_from_str_1 = []
for sym in "my_string":
    list_from_str_1.append(sym + "*")
print(list_from_str_1)

print()

list_from_str_2 = [sym * 5 for sym in 'abcd']
print(list_from_str_2)

list_from_str_3 = []
for sym in 'abcd':
    list_from_str_3.append(sym * 5)
print(list_from_str_3)

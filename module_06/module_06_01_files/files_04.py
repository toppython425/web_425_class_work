# file = open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8')
# content = file.read()
# file.close()
# print(content)
# print()
#
# with open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8') as file:
#     content = file.read()
# print(content)
# print()
#
# file = open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8')
# for line in file:
#     print(line)
# file.close()
# print()
#
# with open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8') as file:
#     for line in file:
#         print(line)
# print()


file = open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8')
for line in file:
    print(line, end='')
file.close()
print()
print()

with open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')
print()
print()

with open(r'test_path_1\test_1.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip())
print()


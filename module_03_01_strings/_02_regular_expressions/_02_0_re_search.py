import re

my_str = "abcd abc egfd"
my_reg = r'\w{4}'
my_reg_comp = re.compile(r'\w{4}')
match = re.search(my_reg_comp, my_str)
print(match)

print(match.group())

my_str_1 = "abcd abc 123 egfd 456"
my_reg_1 = re.compile(r'\d{3}')
match_1 = re.search(my_reg_1, my_str_1)
print(match_1)
print(match_1.group())

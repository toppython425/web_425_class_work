import re

# my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
# my_reg = re.compile(r'А1 \+375\(029\)(\d\d\d\d\d\d\d); МТС \+375\(033\)(\d\d\d\d\d\d\d)')
#
# match_1 = re.search(my_reg, my_str)
# print(match_1)
# print(match_1.group())
# print(match_1.group(1))
# print(match_1.group(2))


my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
my_reg = re.compile(r'А1 \+375\((\d{1,3})\)(\d{7}); МТС \+375\((\d{1,3})\)(\d{7})')

match_2 = re.search(my_reg, my_str)
# print(match_2)
# print(match_2.group())
# print(match_2.group(1))
# print(match_2.group(2))
# print(match_2.group(3))
# print(match_2.group(4))

print(match_2.group(1, 2))
print(match_2.group(3, 4))

# print(match_2.start(), match_2.end())
# print(match_2.start(0), match_2.end(0))
print(match_2.start(1), match_2.end(1))
print(match_2.start(2), match_2.end(2))
print(match_2.start(3), match_2.end(3))
print(match_2.start(4), match_2.end(4))
print()
# print(match_2.span())
print(match_2.span(1))
print(match_2.span(2))
print(match_2.span(3))
print(match_2.span(4))




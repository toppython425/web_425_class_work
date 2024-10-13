import re

my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
my_reg = re.compile(r'А1 \+375\((\d{1,3})\)(\d{7}); МТС \+375\((\d{1,3})\)(\d{7})')
print(re.match(my_reg, my_str))


my_str = """Мои номера телефонов: А1 +375(029)6234567; МТС +375(033)3334455"""
my_reg_1 = re.compile(r'Мои номера телефонов: А1 \+375\((\d{1,3})\)(\d{7}); МТС \+375\((\d{1,3})\)(\d{7})')
print(re.match(my_reg_1, my_str))
print(bool(re.match(my_reg_1, my_str)))
match_1 = re.match(my_reg_1, my_str)
print(match_1.group())
print(match_1.group(1))
print(match_1.group(2))
print(match_1.group(3))
print(match_1.group(4))

my_reg_2 = re.compile(r'Мои номера телефонов: А1 \+375\((\d{1,3})\)(\d{7})')
match_2 = re.match(my_reg_2, my_str)
print(match_2.group())
print(match_2.group(1))
print(match_2.group(2))

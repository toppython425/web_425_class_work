import re

# my_str = """2024 Календарь соревнований:
# 07.04.2024 - Гран При Японии;
# 21.04.2024 - Гран При Китая."""
#
# new_str = re.sub(r'[-;.:]', '**', my_str)
# print(new_str)


my_str = """2024 Календарь соревнований:
07.04.2024 - Гран При Японии,
21.04.2024 - Гран При Китая;
05.05.2024 - Гран При Майами."""

my_str_list = re.split(r'[,;\n]+', my_str)
print(my_str_list)

for my_str in my_str_list:
    print(my_str)

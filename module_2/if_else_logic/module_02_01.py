# print("1 == 1", 1 == 1)
# print(1 == 2)
# print(1 != 1)
# print(1 != 2)
# print(1 > 1)
# print(1 > 2)
# print(2 > 1)
# print(1 < 1)
# print(2 < 1)
# print(1 < 2)
# print(1 >= 1)
# print(1 >= 2)
# print(2 >= 1)
# print(1 <= 1)
# print(1 <= 2)
# print(2 <= 1)
#
#
# print(1 == 2 or 2 == 2)


# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(0))
# print(bool(0.0))
# print(bool(None))
# print(bool('Some str'))
# print(bool(['item_1', 'item_2']))
# print(bool(('item_1', 'item_2')))
# print(bool({'item_1', 'item_2'}))
# print(bool({'k1': 'v1', 'k2': 'v2'}))
# print(bool(1))
# print(bool(0.5))

# competent = True
# responsible = True
#
# print(competent and responsible)
#
# competent = True
# responsible = False
#
# print(competent and responsible)
#
# competent = False
# responsible = True
#
# print(competent and responsible)
#
# competent = False
# responsible = True
#
# print(competent or responsible)
#
#
# competent = True
# responsible = False
#
# print(competent or responsible)
#
# competent = False
# responsible = False
# print(competent or responsible)

#
# previosly_fired = True
# print(not previosly_fired)
#
#
# previosly_fired = False
# print(not previosly_fired)


time = int(input("Введите время в часах: ")) % 24
luggage = False
ticket = False
money = True

print(money or ticket and not luggage and time > 6)
print((money or ticket) and not luggage and time > 6)
print(not luggage and time > 6 and money or ticket)

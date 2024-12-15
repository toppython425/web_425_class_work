import copy


class SampleClass:
    def __init__(self, val):
        self.val = val


obj1 = SampleClass(0)
obj2 = SampleClass(2)
obj3 = obj1
# obj3 = copy.deepcopy(obj1) #  создание копии объекта


print(obj1 is obj2)
print(obj2 is obj3)
print(obj1 is obj3)
print(obj3 is obj1)

print(obj1.val, obj2.val, obj3.val)
obj3.val = 5
print(obj1.val, obj2.val, obj3.val)

str_1 = "У Мерри был "
str_2 = "У Мерри был барашек"
str_1 += "барашек"
str_3 = str_1
print(str_1 == str_2, str_1 is str_2, str_1 == str_3, str_1 is str_3)

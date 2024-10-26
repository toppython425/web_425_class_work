# yield

def func(n):
    for i in range(n):
        return i


print(func(10))
print()


def func_1(n):
    for i in range(n):
        yield i


for value in func_1(10):
    print(value)

[print(value) for value in func_1(5)]
print()

def degrees_of_2(n):
    degree = 1
    for i in range(n):
        yield degree
        degree *= 2


[print(value) for value in degrees_of_2(10)]

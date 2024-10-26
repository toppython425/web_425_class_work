import math
from math import ceil, floor, trunc

x = 3.4
y = 5.6

print("Верхнее округление", ceil(x), ceil(y))
print("Верхнее округление", ceil(-x), ceil(-y))
print("Нижнее округление", floor(x), floor(y))
print("Нижнее округление", floor(-x), floor(-y))
print("Усеченное до целого числа", trunc(x), trunc(y))
print("Усеченное до целого числа", trunc(-x), trunc(-y))
print("Факториал", math.factorial(5))
print("Гипотенуза", math.hypot(3, 4))

print(round(5.12345, 3))
print(round(5.62645, 2))

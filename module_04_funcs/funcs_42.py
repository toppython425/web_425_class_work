# def get_total_check(prices, tip=0):
#     check_sum = sum(prices)
#     total_sum = check_sum * (100 + tip) / 100
#     return total_sum
#
#
# total_0 = get_total_check([1000, 3000, 500])
# total_10 = get_total_check([1000, 3000, 500], 10)
#
# print(f"Итого: {total_0}")
# print(f"Итого: {total_10}")

def get_total_paint(width, height, consumption=0.2, layers=2):
    total_paint = width * height * consumption * layers
    return round(total_paint, 2)


print(f"Итого литров необходимо: {get_total_paint(3, 4)}")
print(f"Итого литров необходимо: {get_total_paint(3, 4, 0.4)}")
print(f"Итого литров необходимо: {get_total_paint(3, 4, 0.2, 3)}")
print(f"Итого литров необходимо: {get_total_paint(width=3, height=4, layers=3)}")

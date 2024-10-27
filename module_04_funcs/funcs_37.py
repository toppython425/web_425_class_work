def get_sum_with_tax(value, tax_percentage):
    total = value + value * tax_percentage / 100
    return total


my_total = get_sum_with_tax(10000, 13)
print(my_total)
print(get_sum_with_tax(10000, 13))

my_sum = 15000
my_tax = 9

my_total_sum = get_sum_with_tax(my_sum, my_tax)
print(f"Cумма с налогом {my_total_sum}")

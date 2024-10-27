def get_calc_sum(numbers: list):
    calc_sum = 0
    for number in numbers:
        calc_sum += int(number)
    return calc_sum


def main():
    user_input = input('Введите числа через пробел: ')
    numbers_list = user_input.split(" ")
    result = get_calc_sum(numbers_list)
    print(result)


main()

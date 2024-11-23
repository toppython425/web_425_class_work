def get_shopping_data(filename, items_count=0, items_sum=0):
    row_index = 0
    with open(filename, encoding='utf-8') as file:
        for item_data in file:
            row_index += 1
            if item_data.count(':') < 2:
                print(f'В строке {row_index} есть ошибка!')
                continue
            temp_data = item_data.strip().split(':')
            # print(temp_data)
            item, quantity, price = temp_data
            items_count += 1
            items_sum += float(price) * float(quantity)
    return items_count, items_sum


my_count, my_sum = get_shopping_data(r'test_path_2/shopping.txt')
print(f'В списке {my_count} товаров. Сумма {my_sum} рублей.')






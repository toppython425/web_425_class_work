# shopping_list = ["молоко", "печенье", "хлопья", "шоколад", "яблоки"]
# product_1 = input("Продукт для удаления: ")
# product_2 = input("Продукт для удаления: ")
# product_3 = input("Продукт для удаления: ")
#
# for product in shopping_list:
#     if product == product_1 or product == product_2 or product == product_3:
#         shopping_list.remove(product)
#
# print(shopping_list)


# medications = ["Пепамицин", "Дилитарил", "Флоутолар", "Россум-лайт"]
#
# indices = input("Введите два индекса: ").split()
# print(indices)
# index1, index2 = int(indices[0]), int(indices[1])
# # index1 = int(indices[0])
# # index2 = int(indices[1])
#
# del medications[index1]
#
# if index2 > index1:
#     index2 -= 1
#
# del medications[index2]
#
# for med in medications:
#     print(med)

# guests = ["Алиса", "Борис", "Василий", "Диана", "Георгий"]
# print(guests.pop(0))
# print(guests.pop())
# print(f"Остались: {", ".join(guests)}.")


word_list = []
while len(word_list) != 5:
    word = input("Введите слово не менее чем из 5 букв: ")
    if len(word) < 5:
        print(f"Неверно Вы ввели слово {word} из {len(word)} букв.")
        continue
    else:
        word_list.append(word)


for word in word_list:
    print(word)

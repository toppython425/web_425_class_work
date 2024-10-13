# day = 13
# print("Сегодня пятница, {:10d}".format(day))
#
# day = 13
# print("Сегодня пятница, {:<10d}".format(day))
# print("Сегодня пятница, {:>10d}".format(day))
# print("Сегодня пятница, {:^10d}".format(day))
# print("Сегодня пятница, {:*^10d}".format(day))

# day = 13
# month = 6
# hour = 15
# print("Сегодня пятница, {1:*>10n}.{0:*^5n}.{2:*<10n}".format(month, day, hour))
#
# day = "пятница"
# month = "июнь"
# hour = "утро"
# print("Сегодня пятница, {1:*>10}.{0}.{2:*<10}".format(month, day, hour))

print("Сегодня пятница, {day:10d}.{month}.{hour}".format(month=10, day=13, hour=15))
print("Сегодня пятница, {day:*>10}.{month}.{day_time:*<10}".format(month="июнь", day="пятница", day_time="утро"))

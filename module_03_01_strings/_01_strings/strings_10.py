normal_string = "Эта строка \n- обычная строка"
print(normal_string)

raw_string = r"Эта строка \n- обычная сырая (raw) строка"
print(raw_string)


raw_string_1 = fr"11234\\{raw_string}"
print(raw_string_1)
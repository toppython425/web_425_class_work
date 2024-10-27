def password_protected(password):

    def inner():

        if password == "secret":
            print("Доступ разрешен:)")
            return "Доступ разрешен:)", param
        else:
            print("В доступе отказано:(")
            return "В доступе отказано:(", param

    return inner

param = 25


login = password_protected('secret')
print(login)
result = login()
print(result)

print()
login_1 = password_protected('no_secret')
login_1()

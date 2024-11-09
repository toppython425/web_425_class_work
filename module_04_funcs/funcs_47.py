def get_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['age'])
    print(kwargs['phone'])


get_personal_data(name="Дмитрий", surname="Сульжиц", age=36, phone="+375(29)1112233")
get_personal_data(surname="Сульжиц", name="Дмитрий", age=36, phone="+375(29)1112233")

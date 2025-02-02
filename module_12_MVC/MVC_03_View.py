class MarksView:
    def __init__(self, controller):
        self.controller = controller

    def display_default_action(self):
        print(self.controller.get_default_action())

    def display_marks_auth(self, user_role='user'):
        result = self.controller.get_marks_auth(user_role)
        if result == 'Forbidden!':
            print(result)
            return None
        if result:
            for item in result:
                print(f'{item['course']} оценка: {item['mark']}')
        else:
            print('Нет данных')

    def display_only_courses_list(self):
        result = self.controller.get_only_courses_list()
        if result:
            print("Список курсов:")
            for item in result:
                print(item, end=' ')
            print()
        else:
            print('Курсов нет!')

    def display_only_marks_list(self):
        result = self.controller.get_only_marks_list()
        if result:
            print("Список оценок:")
            for item in result:
                print(item, end=' ')
            print()
        else:
            print('Оценок нет!')

    def display_all_data_list(self):
        result = self.controller.get_all_data_list()
        if result:
            print(result)
        else:
            print('Нет данных!')

    def display_add_mark(self, course, mark, filename, user_role='user'):
        if not isinstance(mark, int):
            print('Неверный тип данных')
            return
        result = self.controller.add_mark(course, mark, filename, user_role)
        if result == 'Forbidden!':
            print('Forbidden!')
        else:
            print(result)
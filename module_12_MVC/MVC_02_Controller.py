class MarksController:
    def __init__(self, model):
        self.model = model

    def get_default_action(self):
        return 'Добро пожаловать на главную страницу!'

    def get_marks_auth(self, user_role='user'):
        if user_role in ['admin', 'user']:
            if self.model.get_marks():
                return self.model.get_marks()
            return None
        return 'Forbidden!'

    def get_only_courses_list(self):
        courses = []
        data = self.model.get_marks()
        if data:
            for element in data:
                courses.append(element['course'])
            return courses
        return None

    def get_only_marks_list(self):
        marks = []
        data = self.model.get_marks()
        if data:
            for element in data:
                marks.append(element['mark'])
            return marks
        return None

    def get_all_data_list(self):
        if self.model.get_marks():
            return self.get_only_courses_list(), self.get_only_marks_list()
        return None

    def add_mark(self, course, mark, filename, user_role='user'):
        if user_role != 'admin':
            return 'Forbidden!'
        elif not isinstance(mark, int):
            return 'Неверный тип данных'
        self.model.add_mark(course, mark, filename)
        return "Оценка успешно добавлена!"

    # @staticmethod
    # def is_authorise(user_role='user'):
    #     if user_role in ['admin', 'user']:
    #         return True
    #     return False

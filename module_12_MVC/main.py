from MVC_01_Model import MarksModel
from MVC_02_Controller import MarksController
from MVC_03_View import MarksView

if __name__ == '__main__':
    model = MarksModel()
    controller = MarksController(model)
    view = MarksView(controller)

    view.display_default_action()
    view.display_marks_auth('anonymous')
    view.display_marks_auth()
    view.display_only_courses_list()
    view.display_only_marks_list()
    view.display_all_data_list()

    view.display_add_mark('HTML', 10, 'marks_file.json', 'admin')
    view.display_add_mark('CSS', 12, 'marks_file.json', 'admin')
    view.display_add_mark('JavaScript', '11', 'marks_file.json', 'admin')
    view.display_add_mark('Python', 9, 'marks_file.json')
    print()

    view.display_marks_auth()
    view.display_only_courses_list()
    view.display_only_marks_list()
    view.display_all_data_list()

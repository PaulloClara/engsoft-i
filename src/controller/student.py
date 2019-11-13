class Student:

    def __init__(self, controller):
        self.__controller = controller

    def browse_file_button(self):
        pass

    def load_student_list(self):
        view = self.__controller.view.student
        model = self.__controller.model.student

        for student in model.students:
            view.student_list.create_student_label(student_name=student)

    def mounted(self):
        self.load_student_list()

from src.utils.tk import UI
from src.view.student.student_list import StudentList


class Student(UI.Container):

    def __init__(self, master, controller):
        super().__init__(master=master)
        self.pack(side='bottom')

        self.__controller = controller

        self.student_list = None

        self._create_student_list()

    def _create_student_list(self):
        self.student_list = StudentList(master=self)

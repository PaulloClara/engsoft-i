from src.store import Store
from src.utils import Utils

from src.model.student import Student
from src.model.activity import Activity


class Model:

    def __init__(self, controller):
        self.__controller = controller

        self.store = Store()
        self.student = Student(model=self, controller=self.__controller)
        self.activity = Activity(controller=self.__controller, store=self.store)

    def raffle(self, defs):
        students = self.student.students
        activities = self.activity.activities

        if not students:
            return 'Lista de estudantes vazia', None, None

        if not activities:
            return 'Lista de atividades vazia', None, None

        if defs and defs['type'] == 'student':
            student = defs['value']
        else:
            student = students[Utils.get_random_int(0, len(students)-1)]

        if defs and defs['type'] == 'activity':
            activity = defs['value']
        else:
            activity = activities[Utils.get_random_int(0, len(activities)-1)]

        return None, student, activity

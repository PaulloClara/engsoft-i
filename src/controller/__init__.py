from src.utils import Utils

from src.controller.navbar import Navbar
from src.controller.student import Student
from src.controller.activity import Activity


class Controller:

    def __init__(self):
        self.view = None
        self.model = None

        self.navbar = None
        self.student = None
        self.activity = None

    def start(self, model, view):
        self.view = view
        self.model = model

        self.navbar = Navbar(controller=self)
        self.student = Student(controller=self)
        self.activity = Activity(controller=self)

        self.view.start()

    def raffle_button(self, defs={}):
        students = self.model.student.students
        activities = self.model.activity.activities

        if not students:
            self.view.create_error_window(error='Lista de estudantes vazia')
            return

        if not activities:
            self.view.create_error_window(error='Lista de atividades vazia')
            return

        if defs and defs['type'] == 'student':
            student = defs['value']
        else:
            student = students[Utils.get_random_int(0, len(students)-1)]

        if defs and defs['type'] == 'activity':
            activity = defs['value']
        else:
            activity = activities[Utils.get_random_int(0, len(activities)-1)]

        self.view.create_raffle_window(
            student=student, activity=activity['title'])

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
        error, student, activity = self.model.raffle(defs=defs)

        if error:
            self.view.create_error_window(error=error)
            return

        self.view.create_raffle_window(
            student=student, activity=activity['title'])

from src.controller.navbar import Navbar
from src.controller.activity import Activity
from src.controller.student import Student


class Controller:

    def __init__(self):
        self.view = None
        self.model = None

        self.navbar = None
        self.activity = None
        self.student = None

    def start(self, model, view):
        self.view = view
        self.model = model

        self.navbar = Navbar(controller=self)
        self.activity = Activity(controller=self)
        self.student = Student(controller=self)

        self.view.start()

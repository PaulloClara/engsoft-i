from src.utils.tk import TKUtils

from src.view.group import Group
from src.view.navbar import Navbar
from src.view.student import Student
from src.view.activity import Activity

from src.view.error_window import ErrorWindow
from src.view.raffle_window import RaffleWindow


class View(TKUtils.Window()):

    def __init__(self, controller):
        super().__init__()

        self.__controller = controller

        self.title('StuKi®')
        self.geometry('1200x600')
        self.resizable(0, 0)

        self.group = None
        self.navbar = None
        self.student = None
        self.activity = None

        self.error_window = None
        self.raffle_window = None

        self.active_container = ''

    def start(self):
        self._create_navbar()
        self.create_student_container()

        self.mainloop()

    def _create_navbar(self):
        commands = {}

        commands['group'] = self.__controller.navbar.group_button
        commands['student'] = self.__controller.navbar.student_button
        commands['activity'] = self.__controller.navbar.activity_button

        self.navbar = Navbar(master=self, commands=commands)

    def create_student_container(self):
        commands = {}

        commands['raffle'] = self.__controller.raffle_button

        controller = self.__controller.student
        self.student =\
            Student(master=self, controller=controller, commands=commands)

        self.active_container = 'student'

        self.__controller.student.mounted()

    def create_activity_container(self):
        commands = {}

        commands['raffle'] = self.__controller.raffle_button

        controller = self.__controller.activity
        self.activity =\
            Activity(master=self, controller=controller, commands=commands)

        self.active_container = 'activity'

        self.__controller.activity.mounted()

    def create_group_container(self):
        self.group = Group(master=self)
        self.active_container = 'group'

    def destroy_active_container(self):
        if self.active_container == 'student':
            self.student.destroy()
        elif self.active_container == 'activity':
            self.activity.destroy()
        elif self.active_container == 'group':
            self.group.destroy()

        self.active_container = ''

    def create_error_window(self, error):
        self.error_window = ErrorWindow(error=error)

    def create_raffle_window(self, student, activity):
        self.raffle_window = RaffleWindow(student=student, activity=activity)

from src.utils.tk import UI
from src.view.navbar import Navbar
from src.view.student import Student
from src.view.activity import Activity
from src.view.group import Group


class View(UI.Window):

    def __init__(self, controller):
        super().__init__()

        self.__controller = controller

        self.title('EngSoft')
        self.geometry('800x600')

        self.navbar = None
        self.student = None
        self.activity = None
        self.group = None

        self.active_container = ''

    def start(self):
        self._create_navbar()
        self.create_student_container()

        self.mainloop()

    def _create_navbar(self):
        self.navbar = Navbar(master=self)

        controller = self.__controller.navbar

        self.navbar.student_button.configure(
            command=controller.student_button)
        self.navbar.activity_button.configure(
            command=controller.activity_button)
        self.navbar.group_button.configure(
            command=controller.group_button)

    def create_student_container(self):
        self.student = Student(master=self)
        self.active_container = 'student'

    def create_activity_container(self):
        self.activity = Activity(master=self, controller=self.__controller)

        controller = self.__controller.activity

        self.activity.register_button.configure(
            command=controller.register_button)

        self.active_container = 'activity'

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

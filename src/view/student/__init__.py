from src.utils.tk import UI

from src.view.student.actions import Actions
from src.view.student.list import StudentList


class Student(UI.Container):

    def __init__(self, master, controller, commands):
        super().__init__(master=master)
        self.pack(side='bottom')

        self.commands = commands
        self.__controller = controller

        self.actions = None
        self.student_list = None

        self._create_student_list()
        self._create_actions()

    def _create_student_list(self):
        commands = {}

        commands['raffle'] = self.commands['raffle']

        if not self.student_list:
            self.student_list = StudentList(master=self, commands=commands)

    def _create_actions(self):
        commands = {}

        commands['raffle'] = self.commands['raffle']
        commands['browse_file'] = self.__controller.browse_file_button

        self.actions = Actions(master=self, commands=commands)

from src.utils.tk import UI

from src.view.activity.actions import Actions
from src.view.activity.list import ActivitiesList
from src.view.activity.register import RegisterWindow


class Activity(UI.Container):

    def __init__(self, master, controller, commands):
        super().__init__(master=master)
        self.pack(side='bottom')

        self.commands = commands
        self.__controller = controller

        self.actions = None
        self.activities_list = None
        self.register_window = None

        self._create_activities_list()
        self._create_actions()

    def _create_actions(self):
        commands = {}

        commands['raffle'] = self.commands['raffle']
        commands['register'] = self.__controller.register_button

        self.actions = Actions(master=self, commands=commands)

    def _create_activities_list(self):
        commands = {}

        commands['raffle'] = self.commands['raffle']
        commands['remove'] = self.__controller.remove_activity_button

        if not self.activities_list:
            self.activities_list =\
                ActivitiesList(master=self, commands=commands)

    def destroy_activities_list(self):
        for activity in self.activities_list.label_list:
            activity.destroy()

        self.activities_list.label_list = []

    def create_register_window(self):
        commands = {}
        commands['submit_form'] = self.__controller.submit_form_button
        commands['cancel_form'] = self.__controller.cancel_form_button

        self.register_window = RegisterWindow(commands=commands)

    def destroy_register_window(self):
        self.register_window.destroy()
        self.register_window = None

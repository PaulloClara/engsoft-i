from src.utils.tk import UI
from src.view.activity.actions import Actions
from src.view.activity.list import ActivitiesList
from src.view.activity.register import RegisterWindow


class Activity(UI.Container):

    def __init__(self, master, controller):
        super().__init__(master=master)
        self.pack(side='bottom')

        self.__controller = controller

        self.actions = None
        self.activities_list = None
        self.register_window = None

        self._create_activities_list()
        self._create_actions()

    def _create_activities_list(self):
        self.activities_list = ActivitiesList(master=self)

    def _create_actions(self):
        commands = {}
        commands['raffle'] = self.__controller.raffle_button
        commands['register'] = self.__controller.register_button

        self.actions = Actions(master=self, commands=commands)

    def create_register_window(self):
        commands = {}
        commands['submit_form'] = self.__controller.submit_form_button
        commands['cancel_form'] = self.__controller.cancel_form_button

        self.register_window = RegisterWindow(commands=commands)

    def destroy_register_window(self):
        self.register_window.destroy()
        self.register_window = None

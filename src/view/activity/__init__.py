from src.utils.tk import UI
from src.view.activity.register import RegisterWindow


class Activity(UI.Container):

    def __init__(self, master, controller):
        super().__init__(master=master)
        self.pack()

        self.__controller = controller

        self.register_window = None
        self.register_button = None

        self._create_register_button()

    def _create_register_button(self):
        configs = {}

        configs['text'] = 'Cadastrar Atividade'
        configs['width'] = 20

        self.register_button = UI.get_button(master=self, cnf=configs)

    def create_register_window(self):
        self.register_window = RegisterWindow()

        controller = self.__controller.activity

        self.register_window.form.cancel_button.configure(
            command=controller.cancel_form_button)

        self.register_window.form.submit_button.configure(
            command=controller.submit_form_button)

    def destroy_register_window(self):
        self.register_window.destroy()
        self.register_window = None

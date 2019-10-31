from src.utils.tk import UI


class Navbar(UI.Container):

    def __init__(self, master):
        super().__init__(master=master)
        self.pack()

        self.student_button = None
        self.activity_button = None
        self.group_button = None

        self.create_student_button()
        self.create_activity_button()
        self.create_group_button()

    def create_student_button(self):
        configs, pack = {}, {}

        configs['text'] = 'Alunos'
        configs['bg'] = 'red'

        pack['side'] = 'left'

        self.student_button = UI.get_button(
            master=self,
            cnf=configs,
            pack=pack
        )

    def create_activity_button(self):
        configs, pack = {}, {}

        configs['text'] = 'Atividades'
        configs['bg'] = 'blue'
        configs['width'] = 20

        pack['side'] = 'left'

        self.activity_button = UI.get_button(
            master=self,
            cnf=configs,
            pack=pack
        )

    def create_group_button(self):
        configs, pack = {}, {}

        configs['text'] = 'Grupos'
        configs['bg'] = 'green'

        pack['side'] = 'left'

        self.group_button = UI.get_button(
            master=self,
            cnf=configs,
            pack=pack
        )

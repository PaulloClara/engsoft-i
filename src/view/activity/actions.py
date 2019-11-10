from src.utils.tk import UI


class Actions(UI.Container):

    def __init__(self, master, commands):
        super().__init__(master=master, cnf={'bd': 10})
        self.pack(expand=True)

        self.commands = commands

        self.raffle_button = None
        self.register_button = None

        self._create_raffle_button()
        self._create_register_button()

    def _create_raffle_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Sortear Atividade'
        cnf['bg'] = 'blue'
        cnf['width'] = 20
        cnf['command'] = self.commands['raffle']

        pack['side'] = 'left'

        self.raffle_button = UI.get_button(master=self, cnf=cnf, pack=pack)

    def _create_register_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Cadastrar Atividade'
        cnf['bg'] = 'green'
        cnf['width'] = 20
        cnf['command'] = self.commands['register']

        pack['side'] = 'right'

        self.register_button = UI.get_button(master=self, cnf=cnf, pack=pack)

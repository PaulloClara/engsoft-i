from src.utils.tk import TKUtils


class Actions(TKUtils.Container()):

    def __init__(self, master, commands):
        super().__init__(master=master, cnf={'bd': 10})
        self.pack(expand=True)

        self.commands = commands

        self.raffle_button = None
        self.browse_file_button = None

        self._create_raffle_button()
        self._create_browse_file_button()

    def _create_raffle_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Sortear Aluno'
        cnf['bg'] = 'blue'
        cnf['width'] = 20
        cnf['command'] = self.commands['raffle']

        pack['side'] = 'left'

        self.raffle_button = TKUtils.get_button(master=self, cnf=cnf, pack=pack)

    def _create_browse_file_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Procurar CSV'
        cnf['bg'] = 'green'
        cnf['width'] = 20
        cnf['command'] = self.commands['browse_file']

        pack['side'] = 'right'

        self.register_button = TKUtils.get_button(master=self, cnf=cnf, pack=pack)

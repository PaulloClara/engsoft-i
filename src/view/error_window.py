from src.utils.tk import UI


class ErrorWindow(UI.Window):

    def __init__(self, error):
        super().__init__()

        self.title('Janela de Erro')
        self.geometry(f'{len(error) * 16}x140')
        self.resizable(0, 0)

        self.error_msg = error

        self.container = None
        self.error_label = None
        self.confirm_button = None

        self._create_container()

    def _create_container(self):
        cnf = {}
        cnf['bd'] = 10

        self.container = UI.get_container(master=self, cnf=cnf)

        self._create_error_label()
        self._create_confirm_button()

    def _create_error_label(self):
        cnf, pack = {}, {}

        cnf['text'] = self.error_msg
        cnf['fg'] = 'red'
        cnf['font'] = ('arial', 16, 'bold')

        pack['pady'] = 10

        self.error_label = UI.get_label(master=self, cnf=cnf, pack=pack)

    def _create_confirm_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'OK'
        cnf['bg'] = 'green'
        cnf['command'] = self.destroy

        pack['pady'] = 25
        pack['side'] = 'bottom'

        self.confirm_button = UI.get_button(master=self, cnf=cnf, pack=pack)

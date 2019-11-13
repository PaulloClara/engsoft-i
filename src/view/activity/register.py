from src.utils.tk import UI


class RegisterWindow(UI.Window):

    def __init__(self, commands):
        super().__init__()

        self.commands = commands

        self.form = None

        self.title('Cadastrar Atividade')
        self.geometry('400x320')
        self.resizable(0, 0)

        self._create_form()

    def _create_form(self):
        commands = {}
        commands['submit'] = self.commands['submit_form']
        commands['cancel'] = self.commands['cancel_form']

        self.form = Form(master=self, commands=commands)

    def get_form(self):
        fields = {}

        fields['desc'] = self.form.desc_field['input'].get()
        fields['title'] = self.form.title_field['input'].get()
        fields['deadline'] = self.form.deadline_field['input'].get()

        return fields


class Form(UI.Container):

    def __init__(self, master, commands):
        super().__init__(master=master, cnf={'bd': 10})
        self.pack()

        self.commands = commands

        self.desc_field = {}
        self.title_field = {}
        self.deadline_field = {}
        self.submit_button = None
        self.cancel_button = None

        self._create_title_field()
        self._create_desc_field()
        self._create_deadline_field()
        self._create_submit_button()
        self._create_cancel_button()

    def _create_title_field(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Titulo'
        cnf['pady'] = 4

        grid['row'] = 0
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.title_field['label'] =\
            UI.get_label(master=self, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 0
        grid['column'] = 1

        self.title_field['input'] =\
            UI.get_input(master=self, cnf=cnf, grid=grid)

    def _create_desc_field(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Descrição'
        cnf['pady'] = 4

        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.desc_field['label'] = UI.get_label(master=self, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 1
        grid['column'] = 1

        self.desc_field['input'] = UI.get_input(master=self, cnf=cnf, grid=grid)

    def _create_deadline_field(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Data de Entrega   '
        cnf['pady'] = 4

        grid['row'] = 2
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.deadline_field['label'] =\
            UI.get_label(master=self, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 2
        grid['column'] = 1

        self.deadline_field['input'] =\
            UI.get_input(master=self, cnf=cnf, grid=grid)

    def _create_cancel_button(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Cancelar'
        cnf['bg'] = 'red'
        cnf['command'] = self.commands['cancel']

        grid['row'] = 3
        grid['column'] = 0
        grid['sticky'] = 'W'
        grid['pady'] = 350 - self.winfo_screenmmheight()

        self.cancel_button = UI.get_button(master=self, cnf=cnf, grid=grid)

    def _create_submit_button(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Salvar'
        cnf['bg'] = 'green'
        cnf['command'] = self.commands['submit']

        grid['row'] = 3
        grid['column'] = 1
        grid['sticky'] = 'E'
        grid['pady'] = 350 - self.winfo_screenmmheight()

        self.submit_button = UI.get_button(master=self, cnf=cnf, grid=grid)

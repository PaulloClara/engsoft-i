from src.utils.tk import UI


class RegisterWindow(UI.Window):
    def __init__(self):
        super().__init__()

        self.title('Cadastrar Atividade')
        self.geometry('400x320')
        self.resizable(0, 0)

        self.form = None
        self.error = None

        self._create_form()

    def _create_form(self):
        self.form = Form(master=self)

    def get_form(self):
        _inputs = {}

        _inputs['title'] =\
            self.form.title_field['input'].get()
        _inputs['desc'] =\
            self.form.desc_field['input'].get()
        _inputs['deadline'] =\
            self.form.deadline_field['input'].get()

        return _inputs

    def create_error_window(self, error):
        pass


class Form(UI.Container):
    def __init__(self, master):
        super().__init__(master=master, cnf={'bd': 10})
        self.pack()

        self.title_field = {}
        self.desc_field = {}
        self.deadline_field = {}
        self.submit_button = None
        self.cancel_button = None

        self._create_title_field()
        self._create_desc_field()
        self._create_deadline_field()
        self._create_submit_button()
        self._create_cancel_button()

    def _create_title_field(self):
        configs, grid = {}, {}
        configs['text'] = 'Titulo'
        configs['pady'] = 4
        grid['row'] = 0
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.title_field['label'] = UI.get_label(
            master=self,
            cnf=configs,
            grid=grid)

        configs, grid = {}, {}
        grid['row'] = 0
        grid['column'] = 1

        self.title_field['input'] = UI.get_input(
            master=self,
            cnf=configs,
            grid=grid
        )

    def _create_desc_field(self):
        configs, grid = {}, {}
        configs['text'] = 'Descrição'
        configs['pady'] = 4
        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.desc_field['label'] = UI.get_label(
            master=self,
            cnf=configs,
            grid=grid
        )

        configs, grid = {}, {}
        grid['row'] = 1
        grid['column'] = 1

        self.desc_field['input'] = UI.get_input(
            master=self,
            cnf=configs,
            grid=grid
        )

    def _create_deadline_field(self):
        configs, grid = {}, {}
        configs['text'] = 'Data de Entrega   '
        configs['pady'] = 4
        grid['row'] = 2
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.deadline_field['label'] = UI.get_label(
            master=self,
            cnf=configs,
            grid=grid
        )

        configs, grid = {}, {}
        grid['row'] = 2
        grid['column'] = 1

        self.deadline_field['input'] = UI.get_input(
            master=self,
            cnf=configs,
            grid=grid
        )

    def _create_cancel_button(self):
        configs, grid = {}, {}
        configs['text'] = 'Cancelar'
        configs['bg'] = 'red'
        grid['row'] = 3
        grid['column'] = 0
        grid['pady'] = 350 - self.winfo_screenmmheight()
        grid['sticky'] = 'W'

        self.cancel_button = UI.get_button(
            master=self,
            cnf=configs,
            grid=grid
        )

    def _create_submit_button(self):
        configs, grid = {}, {}
        configs['text'] = 'Salvar'
        configs['bg'] = 'green'
        grid['row'] = 3
        grid['column'] = 1
        grid['pady'] = 350 - self.winfo_screenmmheight()
        grid['sticky'] = 'E'

        self.submit_button = UI.get_button(
            master=self,
            cnf=configs,
            grid=grid
        )

from src.utils.tk import TKUtils


class JanelaDeCadastro(TKUtils.Janela()):

    def __init__(self, eventos):
        super().__init__()

        self.eventos = eventos

        self.formulario = None

        self.title('Gerar Grupos')
        self.geometry('400x320')
        self.resizable(0, 0)

        self.criar_formulario()

    def criar_formulario(self):
        eventos = {}

        eventos['confirmar'] = self.eventos['confirmar']
        eventos['cancelar'] = self.eventos['cancelar']

        self.formulario = Formulario(master=self, eventos=eventos)

    def obter_campos(self):
        campos = {}

        campos['nome'] = self.formulario.campo_nome['input'].get()
        campos['quantidade'] = self.formulario.campo_quantidade['input'].get()

        return campos


class Formulario(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master, cnf={'bd': 10})
        self.pack()

        self.eventos = eventos

        self.campo_nome = {}
        self.campo_quantidade = {}
        self.botao_confirmar = None
        self.botao_cancelar = None

        self.criar_campo_nome()
        self.criar_campo_quantidade()
        self.criar_botao_cancelar()
        self.criar_botao_confirmar()

    def criar_campo_nome(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Nome Base'
        cnf['pady'] = 4

        grid['row'] = 0
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_nome['label'] =\
            TKUtils.obter_label(master=self, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 0
        grid['column'] = 1

        self.campo_nome['input'] =\
            TKUtils.obter_input(master=self, cnf=cnf, grid=grid)

    def criar_campo_quantidade(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Quantidade'
        cnf['pady'] = 4

        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_quantidade['label'] =\
            TKUtils.obter_label(master=self, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 1
        grid['column'] = 1

        self.campo_quantidade['input'] =\
            TKUtils.obter_input(master=self, cnf=cnf, grid=grid)

    def criar_botao_cancelar(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Cancelar'
        cnf['bg'] = 'red'
        cnf['command'] = self.eventos['cancelar']

        grid['row'] = 3
        grid['column'] = 0
        grid['sticky'] = 'W'
        grid['pady'] = 350 - self.winfo_screenmmheight()

        self.botao_cancelar = TKUtils.obter_botao(master=self, cnf=cnf, grid=grid)

    def criar_botao_confirmar(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Gerar'
        cnf['bg'] = 'green'
        # cnf['command'] = self.eventos['confirmar']

        grid['row'] = 3
        grid['column'] = 1
        grid['sticky'] = 'E'
        grid['pady'] = 350 - self.winfo_screenmmheight()

        self.botao_confirmar = TKUtils.obter_botao(master=self, cnf=cnf, grid=grid)

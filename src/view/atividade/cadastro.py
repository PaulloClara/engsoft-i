from src.utils.tk import TKUtils
from src.view.janela_de_cadastro import JanelaDeCadastro


class Formulario(JanelaDeCadastro):

    def __init__(self, eventos):
        super().__init__(titulo='Cadastrar Atividade')

        self.eventos = eventos

        self.campo_desc = {}
        self.campo_titulo = {}

        self.criar_campo_titulo()
        self.criar_campo_desc()

        self.criar_botao_cancelar()
        self.criar_botao_confirmar()

    def obter_campos(self):
        campos = {}

        campos['desc'] = self.campo_desc['input'].get()
        campos['titulo'] = self.campo_titulo['input'].get()

        return campos

    def criar_campo_titulo(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Titulo'
        cnf['pady'] = 4

        grid['row'] = 0
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_titulo['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 0
        grid['column'] = 1

        self.campo_titulo['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

    def criar_campo_desc(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Descrição'
        cnf['pady'] = 4

        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_desc['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 1
        grid['column'] = 1

        self.campo_desc['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

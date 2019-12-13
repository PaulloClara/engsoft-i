from src.utils.tk import TKUtils
from src.view.janela_de_cadastro import JanelaDeCadastro


class Formulario(JanelaDeCadastro):

    def __init__(self, eventos):
        super().__init__(titulo='Gerar Grupos')

        self.eventos = eventos

        self.campo_nome = {}
        self.campo_quantidade = {}

    def iniciar(self):
        super().iniciar(texto='Gerar', campos=2)

        self.criar_campo_nome()
        self.criar_campo_quantidade()

    def obter_campos(self):
        campos = {}

        campos['nome'] = self.campo_nome['input'].get()
        campos['quantidade'] = self.campo_quantidade['input'].get()

        return campos

    def criar_campo_nome(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Nome'
        cnf['pady'] = 4

        grid['row'] = 0
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_nome['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        cnf['placeholder'] = 'Segundo Periodo'

        grid['row'] = 0
        grid['column'] = 1

        self.campo_nome['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

    def criar_campo_quantidade(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Quantidade'
        cnf['pady'] = 4

        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_quantidade['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        cnf['placeholder'] = '6'

        grid['row'] = 1
        grid['column'] = 1

        self.campo_quantidade['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

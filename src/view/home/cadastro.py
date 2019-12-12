from src.utils.tk import TKUtils
from src.view.janela_de_cadastro import JanelaDeCadastro


class Formulario(JanelaDeCadastro):

    def __init__(self, eventos):
        super().__init__(titulo='Cadastrar Apresentação')

        self.eventos = eventos

        self.campo_data = {}
        self.campo_duracao = {}

    def iniciar(self):
        super().iniciar(texto='Criar', campos=2)

        self.criar_campo_data()
        self.criar_campo_duracao()

    def obter_campos(self):
        campos = {}
        campos['data'] = self.campo_data['input'].get()
        campos['duracao'] = self.campo_duracao['input'].get()

        return campos

    def criar_campo_data(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Apresentação'
        cnf['pady'] = 4
        cnf['padx'] = 8

        grid['row'] = 0
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_data['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 0
        grid['column'] = 1

        self.campo_data['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

    def criar_campo_duracao(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Duração'
        cnf['pady'] = 4
        cnf['padx'] = 8

        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_duracao['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        grid['row'] = 1
        grid['column'] = 1

        self.campo_duracao['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

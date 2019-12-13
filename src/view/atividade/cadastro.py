from src.utils.tk import TKUtils
from src.view.janela_de_cadastro import JanelaDeCadastro


class Formulario(JanelaDeCadastro):

    def __init__(self, eventos):
        super().__init__(titulo='Cadastrar Atividade')

        self.eventos = eventos

        self.campo_descricao = {}
        self.campo_titulo = {}

    def iniciar(self):
        super().iniciar(texto='Cadastrar', campos=2)

        self.criar_campo_titulo()
        self.criar_campo_descricao()

    def obter_campos(self):
        campos = {}

        campos['titulo'] = self.campo_titulo['input'].get()
        campos['descricao'] = self.campo_descricao['input'].get()

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

        cnf['placeholder'] = 'Capinar um lote'

        grid['row'] = 0
        grid['column'] = 1

        self.campo_titulo['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

    def criar_campo_descricao(self):
        cnf, grid = {}, {}

        cnf['text'] = 'Descrição'
        cnf['pady'] = 4

        grid['row'] = 1
        grid['column'] = 0
        grid['sticky'] = 'W'

        self.campo_descricao['label'] =\
            TKUtils.obter_label(master=self.corpo, cnf=cnf, grid=grid)

        cnf, grid = {}, {}

        cnf['placeholder'] = 'Programar um drone para capinar um lote'

        grid['row'] = 1
        grid['column'] = 1

        self.campo_descricao['input'] =\
            TKUtils.obter_input(master=self.corpo, cnf=cnf, grid=grid)

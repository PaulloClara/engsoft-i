from src.utils.tk import TKUtils
from src.utils.atributo import Atributo

from src.view.janela_cadastro import JanelaDeCadastro


class Formulario(JanelaDeCadastro):

    def __init__(self):
        super().__init__()

        self.defs.cnf['title'] = 'Gerar Grupos'

        self.subelemento.nome = Atributo()
        self.subelemento.nome.label = TKUtils.obter_label()
        self.subelemento.nome.input = TKUtils.obter_input()

        self.subelemento.quantidade = Atributo()
        self.subelemento.quantidade.label = TKUtils.obter_label()
        self.subelemento.quantidade.input = TKUtils.obter_input()

    def iniciar(self):
        super().iniciar()

        self.inicializar_campo_nome()
        self.inicializar_campo_quantidade()

    def obter_campos(self):
        campos = {}

        campos['nome'] = self.subelemento.nome.input.get()
        campos['quantidade'] = self.subelemento.quantidade.input.get()

        return campos

    def inicializar_campo_nome(self):
        self.subelemento.nome.label.defs.cnf['text'] = 'Nome'
        self.subelemento.nome.label.defs.cnf['pady'] = 4

        self.subelemento.nome.label.defs.grid['row'] = 0
        self.subelemento.nome.label.defs.grid['column'] = 0
        self.subelemento.nome.label.defs.grid['sticky'] = 'W'

        self.subelemento.nome.input.defs.cnf['width'] = 30
        self.subelemento.nome.input.defs.mcnf['focus'] = True
        self.subelemento.nome.input.defs.mcnf['placeholder'] = 'Segundo Periodo'

        self.subelemento.nome.input.defs.grid['row'] = 0
        self.subelemento.nome.input.defs.grid['column'] = 1

        self.subelemento.nome.input.iniciar(master=self.subelemento.main)
        self.subelemento.nome.label.iniciar(master=self.subelemento.main)

    def inicializar_campo_quantidade(self):
        self.subelemento.quantidade.label.defs.cnf['text'] = 'Quantidade'
        self.subelemento.quantidade.label.defs.cnf['pady'] = 4

        self.subelemento.quantidade.label.defs.grid['row'] = 1
        self.subelemento.quantidade.label.defs.grid['column'] = 0
        self.subelemento.quantidade.label.defs.grid['sticky'] = 'W'

        self.subelemento.quantidade.input.defs.cnf['width'] = 30
        self.subelemento.quantidade.input.defs.mcnf['placeholder'] = '6'

        self.subelemento.quantidade.input.defs.grid['row'] = 1
        self.subelemento.quantidade.input.defs.grid['column'] = 1

        self.subelemento.quantidade.input.iniciar(master=self.subelemento.main)
        self.subelemento.quantidade.label.iniciar(master=self.subelemento.main)

from src.utils.tk import TKUtils
from src.utils.atributo import Atributo

from src.view.janela_cadastro import JanelaDeCadastro


class Formulario(JanelaDeCadastro):

    def __init__(self):
        super().__init__()

        self.defs.cnf['title'] = 'Cadastrar Atividade'

        self.subelemento.titulo = Atributo()
        self.subelemento.titulo.label = TKUtils.obter_label()
        self.subelemento.titulo.input = TKUtils.obter_input()

        self.subelemento.descricao = Atributo()
        self.subelemento.descricao.label = TKUtils.obter_label()
        self.subelemento.descricao.input = TKUtils.obter_input()

    def iniciar(self):
        super().iniciar()

        self.inicializar_campo_titulo()
        self.inicializar_campo_descricao()

    def obter_campos(self):
        campos = {}

        campos['titulo'] = self.subelemento.titulo.input.get()
        campos['descricao'] = self.subelemento.descricao.input.get()

        return campos

    def inicializar_campo_titulo(self):
        self.subelemento.titulo.label.defs.cnf['pady'] = 4
        self.subelemento.titulo.label.defs.cnf['text'] = 'Titulo'

        self.subelemento.titulo.label.defs.grid['row'] = 0
        self.subelemento.titulo.label.defs.grid['column'] = 0
        self.subelemento.titulo.label.defs.grid['sticky'] = 'W'

        self.subelemento.titulo.input.defs.cnf['width'] = 30
        self.subelemento.titulo.input.defs.mcnf['focus'] = True
        self.subelemento.titulo.input.defs.mcnf['placeholder'] = 'Capinar lote'

        self.subelemento.titulo.input.defs.grid['row'] = 0
        self.subelemento.titulo.input.defs.grid['column'] = 1

        self.subelemento.titulo.label.iniciar(master=self.subelemento.main)
        self.subelemento.titulo.input.iniciar(master=self.subelemento.main)

    def inicializar_campo_descricao(self):
        self.subelemento.descricao.label.defs.cnf['pady'] = 4
        self.subelemento.descricao.label.defs.cnf['text'] = 'Descrição'

        self.subelemento.descricao.label.defs.grid['row'] = 1
        self.subelemento.descricao.label.defs.grid['column'] = 0
        self.subelemento.descricao.label.defs.grid['sticky'] = 'W'

        self.subelemento.descricao.input.defs.cnf['width'] = 30
        self.subelemento.descricao.input.defs.mcnf['placeholder'] =\
            'Programar um drone para capinar um lote'

        self.subelemento.descricao.input.defs.grid['row'] = 1
        self.subelemento.descricao.input.defs.grid['column'] = 1

        self.subelemento.descricao.label.iniciar(master=self.subelemento.main)
        self.subelemento.descricao.input.iniciar(master=self.subelemento.main)

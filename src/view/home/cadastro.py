from src.utils import Utils
from src.utils.tk import TKUtils
from src.utils.atributo import Atributo

from src.view.janela_cadastro import JanelaDeCadastro


class FormularioApresentacao(JanelaDeCadastro):

    def __init__(self):
        super().__init__()

        self.defs.cnf['title'] = 'Cadastrar Apresentação'

        self.subelemento.data = Atributo()
        self.subelemento.data.label = TKUtils.obter_label()
        self.subelemento.data.input = TKUtils.obter_input()

        self.subelemento.duracao = Atributo()
        self.subelemento.duracao.label = TKUtils.obter_label()
        self.subelemento.duracao.input = TKUtils.obter_input()

    def iniciar(self):
        super().iniciar()

        self.inicializar_campo_data()
        self.inicializar_campo_duracao()

    def obter_campos(self):
        campos = {}
        campos['data'] = self.subelemento.data.input.get()
        campos['duracao'] = self.subelemento.duracao.input.get()

        return campos

    def inicializar_campo_data(self):
        self.subelemento.data.label.defs.cnf['text'] = 'Data'
        self.subelemento.data.label.defs.cnf['pady'] = 4

        self.subelemento.data.label.defs.grid['row'] = 0
        self.subelemento.data.label.defs.grid['column'] = 0
        self.subelemento.data.label.defs.grid['sticky'] = 'W'

        self.subelemento.data.input.defs.cnf['width'] = 30
        self.subelemento.data.input.defs.mcnf['focus'] = True
        self.subelemento.data.input.defs.mcnf['placeholder'] =\
            Utils.data_e_hora_atual().split(' ')[0]

        self.subelemento.data.input.defs.grid['row'] = 0
        self.subelemento.data.input.defs.grid['column'] = 1

        self.subelemento.data.input.iniciar(master=self.subelemento.main)
        self.subelemento.data.label.iniciar(master=self.subelemento.main)

    def inicializar_campo_duracao(self):
        self.subelemento.duracao.label.defs.cnf['text'] = 'Duração'
        self.subelemento.duracao.label.defs.cnf['pady'] = 4

        self.subelemento.duracao.label.defs.grid['row'] = 1
        self.subelemento.duracao.label.defs.grid['column'] = 0
        self.subelemento.duracao.label.defs.grid['sticky'] = 'W'

        self.subelemento.duracao.input.defs.cnf['width'] = 30
        self.subelemento.duracao.input.defs.mcnf['placeholder'] = '20'

        self.subelemento.duracao.input.defs.grid['row'] = 1
        self.subelemento.duracao.input.defs.grid['column'] = 1

        self.subelemento.duracao.input.iniciar(master=self.subelemento.main)
        self.subelemento.duracao.label.iniciar(master=self.subelemento.main)


class FormularioTarefa(FormularioApresentacao):

    def __init__(self):
        super().__init__()

        self.defs.cnf['title'] = 'Cadastrar Tarefa'

    def iniciar(self):
        super().iniciar()

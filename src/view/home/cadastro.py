from src.utils import Utils
from src.utils.tk import TKUtils
from src.utils.atributo import Atributo

from src.view.janela_cadastro import JanelaDeCadastro


class FormularioBase(JanelaDeCadastro):

    def __init__(self, campos=2):
        super().__init__(campos)

        self.subelemento.data = Atributo()
        self.subelemento.data.label = TKUtils.obter_label()
        self.subelemento.data.input = TKUtils.obter_input()

        self.subelemento.duracao = Atributo()
        self.subelemento.duracao.label = TKUtils.obter_label()
        self.subelemento.duracao.input = TKUtils.obter_input()

    def iniciar(self):
        super().iniciar()

        self.configurar_campo_data()
        self.configurar_campo_duracao()

        self.subelemento.data.input.iniciar(master=self.subelemento.main)
        self.subelemento.data.label.iniciar(master=self.subelemento.main)
        self.subelemento.duracao.input.iniciar(master=self.subelemento.main)
        self.subelemento.duracao.label.iniciar(master=self.subelemento.main)

    def obter_campos(self):
        campo = {}
        campo['data'] = self.subelemento.data.input.get()
        campo['duracao'] = self.subelemento.duracao.input.get()

        return campo

    def configurar_campo_data(self):
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

    def configurar_campo_duracao(self):
        self.subelemento.duracao.label.defs.cnf['text'] = 'Duração'
        self.subelemento.duracao.label.defs.cnf['pady'] = 4

        self.subelemento.duracao.label.defs.grid['row'] = 1
        self.subelemento.duracao.label.defs.grid['column'] = 0
        self.subelemento.duracao.label.defs.grid['sticky'] = 'W'

        self.subelemento.duracao.input.defs.cnf['width'] = 30
        self.subelemento.duracao.input.defs.mcnf['placeholder'] = '20'

        self.subelemento.duracao.input.defs.grid['row'] = 1
        self.subelemento.duracao.input.defs.grid['column'] = 1


class FormularioApresentacao(FormularioBase):

    def __init__(self):
        super().__init__()

        self.defs.cnf['title'] = 'Cadastrar Apresentação'

    def iniciar(self):
        super().iniciar()


class FormularioTarefa(FormularioBase):

    def __init__(self):
        super().__init__()

        self.defs.cnf['title'] = 'Cadastrar Tarefa'

    def iniciar(self):
        super().iniciar()


class FormularioEvento(FormularioBase):

    def __init__(self):
        super().__init__(campos=3)

        self.defs.cnf['title'] = 'Cadastrar Evento'

        self.subelemento.titulo = Atributo()
        self.subelemento.titulo.label = TKUtils.obter_label()
        self.subelemento.titulo.input = TKUtils.obter_input()

    def iniciar(self):
        super().iniciar()

        self.configurar_campo_titulo()

        self.subelemento.titulo.label.iniciar(master=self.subelemento.main)
        self.subelemento.titulo.input.iniciar(master=self.subelemento.main)

    def obter_campos(self):
        campo = super().obter_campos()
        campo['titulo'] = self.subelemento.titulo.input.get()

        if ' ' in campo['duracao']:
            campo['duracao'] = campo['duracao'].split(' ')[0]

        return campo

    def configurar_campo_titulo(self):
        self.subelemento.titulo.label.defs.cnf['text'] = 'Titulo'
        self.subelemento.titulo.label.defs.cnf['pady'] = 4

        self.subelemento.titulo.label.defs.grid['row'] = 0
        self.subelemento.titulo.label.defs.grid['column'] = 0
        self.subelemento.titulo.label.defs.grid['sticky'] = 'W'

        self.subelemento.titulo.input.defs.cnf['width'] = 30
        self.subelemento.titulo.input.defs.mcnf['placeholder'] = 'Sprint 01'

        self.subelemento.titulo.input.defs.grid['row'] = 0
        self.subelemento.titulo.input.defs.grid['column'] = 1

    def configurar_campo_data(self):
        super().configurar_campo_data()

        self.subelemento.data.label.defs.grid['row'] = 1
        self.subelemento.data.input.defs.grid['row'] = 1

    def configurar_campo_duracao(self):
        super().configurar_campo_duracao()

        self.subelemento.duracao.input.defs.mcnf['placeholder'] = '2 dias'
        self.subelemento.duracao.label.defs.grid['row'] = 2
        self.subelemento.duracao.input.defs.grid['row'] = 2

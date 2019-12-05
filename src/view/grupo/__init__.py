from src.utils.tk import TKUtils
from src.view.grupo.actions import Actions
from src.view.grupo.cadastro import JanelaDeCadastro


class Grupo(TKUtils.Container()):

    def __init__(self, master, controller, eventos):
        super().__init__(master=master)
        self.pack()

        self.eventos = eventos
        self.__controller = controller

        self.actions = None
        self.janela_de_cadastro = None

        self.criar_actions()

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['cadastrar'] = self.__controller.evento_cadastrar

        self.actions = Actions(master=self, eventos=eventos)

    def criar_janela_de_cadastro(self):
        eventos = {}

        eventos['cancelar'] = self.__controller.evento_cancelar_cadastro
        eventos['confirmar'] = self.__controller.evento_confirmar_cadastro

        self.janela_de_cadastro = JanelaDeCadastro(eventos=eventos)

    def destruir_janela_de_cadastro(self):
        self.janela_de_cadastro.destroy()
        self.janela_de_cadastro = None

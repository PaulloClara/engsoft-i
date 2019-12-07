from src.utils.tk import TKUtils

from src.view.atividade.actions import Actions
from src.view.atividade.lista import ListaDeAtividades
from src.view.atividade.cadastro import Formulario


class Atividade(TKUtils.Container()):

    def __init__(self, master, controller, eventos):
        super().__init__(master=master)
        self.pack(side='bottom')

        self.eventos = eventos
        self.__controller = controller

        self.actions = None
        self.lista_de_atividades = None
        self.janela_de_cadastro = None

        self.criar_lista_de_atividades()
        self.criar_actions()

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['cadastrar'] = self.__controller.evento_cadastrar

        self.actions = Actions(master=self, eventos=eventos)

    def criar_lista_de_atividades(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['remover'] = self.__controller.evento_remover_atividade

        if not self.lista_de_atividades:
            self.lista_de_atividades =\
                ListaDeAtividades(master=self, eventos=eventos)

    def destruir_lista_de_atividades(self):
        for atividade in self.lista_de_atividades.atividades:
            atividade.destroy()

        self.lista_de_atividades.atividades = []

    def criar_janela_de_cadastro(self):
        eventos = {}
        eventos['cancelar'] = self.__controller.evento_cancelar_cadastro
        eventos['confirmar'] = self.__controller.evento_confirmar_cadastro

        self.janela_de_cadastro = Formulario(eventos=eventos)

    def destruir_janela_de_cadastro(self):
        self.janela_de_cadastro.destroy()
        self.janela_de_cadastro = None

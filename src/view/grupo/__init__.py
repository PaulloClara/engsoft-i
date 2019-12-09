from src.utils.tk import TKUtils

from src.view.grupo.actions import Actions
from src.view.grupo.cadastro import Formulario
from src.view.grupo.lista import ListaDeGrupos


class Grupo(TKUtils.Container()):

    def __init__(self, master, controller, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.controller = controller

        self.actions = None
        self.lista_de_grupos = None
        self.janela_de_cadastro = None

    def iniciar(self):
        self.criar_actions()
        self.criar_lista_de_grupos()

        self.lista_de_grupos.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_lista_de_grupos(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['remover'] = self.controller.evento_remover_grupo

        self.lista_de_grupos = ListaDeGrupos(master=self, eventos=eventos)

    def destruir_lista_de_grupos(self):
        for grupo in self.lista_de_grupos.grupos:
            grupo.destroy()

        self.lista_de_grupos.grupos = []

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['cadastrar'] = self.controller.evento_cadastrar

        self.actions = Actions(master=self, eventos=eventos)

    def criar_janela_de_cadastro(self):
        eventos = {}

        eventos['cancelar'] = self.controller.evento_cancelar_cadastro
        eventos['confirmar'] = self.controller.evento_confirmar_cadastro

        self.janela_de_cadastro = Formulario(eventos=eventos)
        self.janela_de_cadastro.iniciar()

    def destruir_janela_de_cadastro(self):
        self.janela_de_cadastro.destroy()
        self.janela_de_cadastro = None

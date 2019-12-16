from src.utils.tk import TKUtils

from src.view.home.actions import Actions
from src.view.home.lista import ListaDeElementos
from src.view.home.cadastro import Formulario


class Home(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

        self.controller = controller

        self.actions = None
        self.lista_de_elementos = None
        self.janela_de_cadastro = None

    def iniciar(self):
        self.criar_lista_de_elementos()
        self.criar_actions()

        self.lista_de_elementos.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_lista_de_elementos(self):
        eventos = {}

        eventos['expandir'] = self.controller.evento_expandir_label
        eventos['remover'] = self.controller.evento_remover_apresentacao

        self.lista_de_elementos = ListaDeElementos(master=self, eventos=eventos)

    def destruir_lista_de_elementos(self):
        for elemento in self.lista_de_elementos.elementos:
            elemento.destroy()

        self.lista_de_elementos.elementos = []

    def criar_actions(self):
        eventos = {}

        eventos['ordenar'] = self.controller.evento_ordenar_lista
        eventos['cadastrar'] = self.controller.evento_cadastrar_apresentacao

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

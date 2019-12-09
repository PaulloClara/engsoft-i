from src.utils.tk import TKUtils

from src.view.home.actions import Actions
from src.view.home.lista import ListaDeElementos


class Home(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

        self.controller = controller

        self.actions = None
        self.lista_de_elementos = None

    def iniciar(self):
        self.criar_lista_de_elementos()
        self.criar_actions()

        self.lista_de_elementos.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_lista_de_elementos(self):
        eventos = {}

        eventos['click'] = self.controller.evento_click_no_label
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

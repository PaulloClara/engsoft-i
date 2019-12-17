from src.utils.tk import TKUtils

from src.view.home.actions import Actions
from src.view.home.lista import ListaDeElementos
from src.view.home.cadastro import Formulario


class Home(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

        self.controller = controller

        self.actions = None
        self.lista = None
        self.janela_de_cadastro = None

    def iniciar(self):
        self.criar_listagem_de_elementos()
        self.criar_actions()

        self.lista.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_listagem_de_elementos(self):
        eventos = {}

        eventos['expandir'] = self.controller.eventos.expandir_label
        eventos['remover'] = self.controller.eventos.remover_apresentacao

        self.lista = ListaDeElementos(master=self, eventos=eventos)

    def destruir_lista_de_elementos(self):
        for elemento in self.lista.elementos:
            elemento.destroy()

        self.lista.elementos = []

    def criar_actions(self):
        eventos = {}

        eventos['ordenar'] = self.controller.eventos.ordenar_lista
        eventos['cadastrar'] = self.controller.eventos.cadastrar_apresentacao

        self.actions = Actions(master=self, eventos=eventos)

    def criar_janela_de_cadastro(self):
        eventos = {}

        eventos['cancelar'] = self.controller.eventos.cancelar_cadastro
        eventos['confirmar'] = self.controller.eventos.confirmar_cadastro

        self.janela_de_cadastro = Formulario(eventos=eventos)
        self.janela_de_cadastro.iniciar()

    def destruir_janela_de_cadastro(self):
        self.janela_de_cadastro.destroy()
        self.janela_de_cadastro = None

    def ativar(self):
        self.pack_configure(side='bottom')

    def desativar(self):
        self.pack_forget()

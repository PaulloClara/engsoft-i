from src.utils.tk import TKUtils

from src.view.atividade.actions import Actions
from src.view.atividade.lista import ListaDeAtividades
from src.view.atividade.cadastro import Formulario


class Atividade(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

        self.controller = controller

        self.actions = None
        self.lista = None
        self.janela_de_cadastro = None

    def iniciar(self):
        self.criar_actions()
        self.criar_listagem_de_atividades()

        self.lista.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.controller.eventos.sortear
        eventos['cadastrar'] = self.controller.eventos.cadastrar

        self.actions = Actions(master=self, eventos=eventos)

    def criar_listagem_de_atividades(self):
        eventos = {}

        eventos['sortear'] = self.controller.eventos.sortear
        eventos['remover'] = self.controller.eventos.remover_atividade
        eventos['expandir'] = self.controller.eventos.expandir_label

        self.lista = ListaDeAtividades(master=self, eventos=eventos)

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

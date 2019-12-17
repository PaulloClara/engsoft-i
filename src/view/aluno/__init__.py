from src.utils.tk import TKUtils

from src.view.aluno.actions import Actions
from src.view.aluno.lista import ListaDeAlunos


class Aluno(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

        self.controller = controller

        self.lista = None
        self.actions = None

    def iniciar(self):
        self.criar_actions()
        self.criar_listagem_de_alunos()

        self.lista.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_listagem_de_alunos(self):
        eventos = {}

        eventos['sortear'] = self.controller.eventos.sortear
        eventos['expandir'] = self.controller.eventos.expandir_label

        self.lista = ListaDeAlunos(master=self, eventos=eventos)

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.controller.eventos.sortear
        eventos['arquivo'] = self.controller.eventos.carregar_arquivo

        self.actions = Actions(master=self, eventos=eventos)

    def ativar(self):
        self.pack_configure(side='bottom')

    def desativar(self):
        self.pack_forget()

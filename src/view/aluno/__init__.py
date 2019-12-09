from src.utils.tk import TKUtils

from src.view.aluno.actions import Actions
from src.view.aluno.lista import ListaDeAlunos


class Aluno(TKUtils.Container()):

    def __init__(self, master, controller, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.controller = controller

        self.actions = None
        self.lista_de_alunos = None

    def iniciar(self):
        self.criar_actions()
        self.criar_lista_de_alunos()

        self.lista_de_alunos.iniciar()
        self.actions.iniciar()

        self.pack(side='bottom')

    def criar_lista_de_alunos(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']

        if not self.lista_de_alunos:
            self.lista_de_alunos = ListaDeAlunos(master=self, eventos=eventos)

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['arquivo'] = self.controller.evento_carregar_arquivo

        self.actions = Actions(master=self, eventos=eventos)

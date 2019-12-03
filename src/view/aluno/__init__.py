from src.utils.tk import TKUtils

from src.view.aluno.actions import Actions
from src.view.aluno.lista import ListaDeAlunos


class Aluno(TKUtils.Container()):

    def __init__(self, master, controller, eventos):
        super().__init__(master=master)
        self.pack(side='bottom')

        self.eventos = eventos
        self.__controller = controller

        self.actions = None
        self.lista_de_alunos = None

        self.criar_lista_de_alunos()
        self.criar_actions()

    def criar_lista_de_alunos(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']

        if not self.lista_de_alunos:
            self.lista_de_alunos = ListaDeAlunos(master=self, eventos=eventos)

    def criar_actions(self):
        eventos = {}

        eventos['sortear'] = self.eventos['sortear']
        eventos['arquivo'] = self.__controller.evento_carregar_arquivo

        self.actions = Actions(master=self, eventos=eventos)

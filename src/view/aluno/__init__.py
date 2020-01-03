from src.utils.tk import TKUtils

from src.view.aluno.actions import Actions
from src.view.aluno.listagem import ListaDeAlunos


class Aluno(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['side'] = 'bottom'

        self.actions = Actions()
        self.listagem = ListaDeAlunos()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.actions.iniciar(master=self)
        self.listagem.iniciar(master=self)

        self.ocultar()

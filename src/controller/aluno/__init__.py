from src.controller.aluno.actions import Actions
from src.controller.aluno.listagem import Listagem


class Aluno(Actions, Listagem):

    def __init__(self) -> None:
        Actions.__init__(self)
        Listagem.__init__(self)

    def iniciar(self, controller: object) -> None:
        self.view = controller.view
        self.model = controller.model

        self.cadastrar_tarefa = controller.tarefa.cadastrar

        Actions.configurar(self)
        Listagem.configurar(self)

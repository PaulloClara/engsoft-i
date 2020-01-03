"""Controller do Aluno."""

from src.controller.aluno.actions import Actions
from src.controller.aluno.listagem import Listagem


class Aluno(Actions, Listagem):
    """Classe responsavel por controlar componentes relacionados ao aluno."""

    def __init__(self) -> None:
        """Construtor padrao, define define os atributos view e model."""
        Actions.__init__(self)
        Listagem.__init__(self)

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model

        self.cadastrar_tarefa = controller.tarefa.cadastrar

        Actions.configurar(self)
        Listagem.configurar(self)

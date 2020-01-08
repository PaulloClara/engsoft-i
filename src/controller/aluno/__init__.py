"""Aluno no contexto do Controller."""

from src.controller.aluno.actions import Actions
from src.controller.aluno.listagem import Listagem


class Aluno(Actions, Listagem):
    """Controla os componentes relacionados a camada Aluno em View e Model."""

    def __init__(self) -> None:
        """Inicializa Actions e Listagem da camada Aluno a nivel Controller."""
        Actions.__init__(self)
        Listagem.__init__(self)

    def iniciar(self, controller: object) -> None:
        """Inicializa as configuracoes em Actions e Listagem."""
        self.view = controller.view
        self.model = controller.model

        self.cadastrar_tarefa = controller.tarefa.cadastrar

        Actions.configurar(self)
        Listagem.configurar(self)

"""Controller do Grupo."""

from src.controller.grupo.actions import Actions
from src.controller.grupo.listagem import Listagem
from src.controller.grupo.cadastro import Cadastro


class Grupo(Actions, Listagem, Cadastro):
    """Classe responsavel por gerenciar a View e Model relacionados a Grupo."""

    def __init__(self) -> None:
        """Classe responsavel por gerenciar os componentes de Atividade."""
        Actions.__init__(self)
        Listagem.__init__(self)
        Cadastro.__init__(self)

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model
        self.cadastrar_apresentacao = controller.apresentacao.cadastrar

        Actions.configurar(self)
        Listagem.configurar(self)

    def cadastrar(self, evt) -> None:
        """Evento click do botao cadastrar."""
        self.view.grupo.cadastro.iniciar()
        Cadastro.configurar(self)

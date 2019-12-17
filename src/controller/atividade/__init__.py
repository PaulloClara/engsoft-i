"""Controller da Atividade."""
from src.controller.atividade.eventos import Eventos


class Atividade(object):
    """Classe responsavel por gerenciar os componentes de Atividade.

    Attributes:
        view (View:obj): Objeto root View
        model (Mode:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Classe responsavel por gerenciar os componentes de Atividade.

        Args:
            controller (Controller:obj): Objeto Pai
        """
        self.view = controller.view
        self.model = controller.model

        self.eventos = Eventos(controller=self)

    def carregar_atividades(self) -> None:
        """Busca as atividades no Model e cria os componentes visuais."""
        for atv in self.model.atividade.atividades:
            self.view.atividade.lista.adicionar(atividade=atv)

    def elemento_montado(self) -> None:
        """Disparado quando o componente Atividade da View e montado.

        - Inicia o componente/container visual da Atividade
        - Carrega a listagem das atividades na view
        """
        self.view.atividade.iniciar()
        self.carregar_atividades()

        self.view.atividade.desativar()

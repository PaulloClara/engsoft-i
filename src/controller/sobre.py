"""Controller de Sobre."""


class Sobre(object):
    """Classe responsavel por gerenciar View e Model relacionados a Sobre.

    Attributes:
        view (View:obj): Objeto root View
        model (Model:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Construtor padrao, define view e model.

        Args:
            controller (Controller:obj): Objeto root Controller
        """
        self.view = controller.view
        self.model = controller.model

    def evento_elemento_montado(self) -> None:
        """Evento disparado quando o componente Sobre e montado.

        - Inicia o container Sobre
        """
        self.view.sobre.iniciar()

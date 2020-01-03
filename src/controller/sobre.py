"""Controller de Sobre."""


class Sobre(object):
    """Classe responsavel por gerenciar View e Model relacionados a Sobre."""

    def __init__(self) -> None:
        """Construtor padrao, define view e model."""
        pass

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model

        self.configurar()

    def configurar(self) -> None:
        """Evento disparado quando o componente Sobre e montado."""
        pass

"""Actions de Aluno no contexto do Controller."""

from src.utils.tipo import Tipo


class Actions(object):
    """Controla os eventos relacionados a View da camada Aluno."""

    def __init__(self) -> None:
        """."""
        pass

    def arquivo(self, evt: Tipo.evento_tk()) -> None:
        """Evento click do botao para carregar arquivo csv."""
        pass

    def configurar(self) -> None:
        """Configura os elementos."""
        self.view.aluno.actions.subelemento.arquivo.evento['<Button-1>'] =\
            self.arquivo

        self.view.aluno.actions.carregar_eventos()

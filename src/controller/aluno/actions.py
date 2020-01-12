from src.utils.tipo import Tipo


class Actions(object):

    def __init__(self) -> None:
        pass

    def arquivo(self, evt: Tipo.evento_tk()) -> None:
        pass

    def configurar(self) -> None:
        self.view.aluno.actions.subelemento.arquivo.evento['<Button-1>'] =\
            self.arquivo

        self.view.aluno.actions.carregar_eventos()

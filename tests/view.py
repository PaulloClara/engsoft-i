from src.view import View
from tests.exception import ExceptionNoTeste


class TView(object):

    def __init__(self, loop: int) -> None:
        self.loop = loop
        self.view = View()

    def iniciar(self) -> None:
        pass

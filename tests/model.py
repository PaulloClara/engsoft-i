from src.model import Model
from tests.exception import ExceptionNoTeste


class TModel(object):

    def __init__(self, loop: int) -> None:
        self.loop = loop
        self.model = Model()

    def iniciar(self) -> None:
        pass

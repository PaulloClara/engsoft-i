from src.store import Store
from tests.exception import ExceptionNoTeste


class TStore(object):

    def __init__(self, loop: int) -> None:
        self.loop = loop
        self.store = Store()

    def iniciar(self) -> None:
        pass

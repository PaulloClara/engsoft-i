from src.view import View
from src.model import Model
from src.controller import Controller


class TController(object):

    def __init__(self, loop: int) -> None:
        self.loop = loop

    def iniciar(self) -> None:
        pass

    def inicializacao(self) -> None:
        view = View()
        model = Model()
        controller = Controller()

        view.iniciar()

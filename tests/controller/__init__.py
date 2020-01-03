from src.view import View
from src.model import Model
from src.controller import Controller


class TesteDoController:

    def __init__(self, loop):
        self.loop = loop

    def iniciar(self):
        pass

    def inicializacao(self):
        view = View()
        model = Model()
        controller = Controller()

        view.iniciar()

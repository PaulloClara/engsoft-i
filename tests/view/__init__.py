from src.view import View
from src.model import Model
from src.controller import Controller


class TesteDaView:

    def __init__(self, loop):
        self.loop = loop

        model = Model()
        self.view = View()
        controller = Controller()

    def iniciar(self):
        pass

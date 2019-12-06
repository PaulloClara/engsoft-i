from src.view import View
from src.model import Model
from src.controller import Controller


class TesteDaView:

    def __init__(self, loop):
        self.loop = loop

        controller = Controller()
        model = Model(controller=controller)
        self.view = View(controller=controller)
        controller.segundo_init(model=model, view=self.view)

    def iniciar(self):
        pass

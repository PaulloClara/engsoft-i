from src.view import View
from src.model import Model
from src.controller import Controller


class TesteDoController:

    def __init__(self, loop):
        self.loop = loop

        self.controller = Controller()
        model = Model(controller=self.controller)
        view = View(controller=self.controller)
        self.controller.segundo_init(model=model, view=view)

    def iniciar(self):
        pass

from src.utils import Utils

from src.view import View
from src.model import Model
from src.controller import Controller

from tests import Tests


if __name__ == '__main__':
    if Utils.verificar_modo_teste():
        tests = Tests()
        tests.iniciar()
    else:
        controller = Controller()
        model = Model(controller=controller)
        view = View(controller=controller)

        controller.iniciar(model=model, view=view)

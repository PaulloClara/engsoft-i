from sys import argv as args

from src.view import View
from src.model import Model
from src.controller import Controller

from tests import Tests


if __name__ == '__main__':
    if '--test' in args:
        tests = Tests()
        tests.start()
    else:
        controller = Controller()
        model = Model(controller=controller)
        view = View(controller=controller)

        controller.start(model=model, view=view)

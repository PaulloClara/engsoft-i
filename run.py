from src.view import View
from src.model import Model
from src.controller import Controller


if __name__ == '__main__':
    controller = Controller()
    model = Model(controller=controller)
    view = View(controller=controller)

    controller.start(model=model, view=view)

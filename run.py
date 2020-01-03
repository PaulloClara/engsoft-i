from src.utils.env import Env

from src.view import View
from src.model import Model
from src.controller import Controller

from tests import Tests


if __name__ == '__main__':
    if Env.modo_teste():
        Tests().iniciar()
        exit()

    view = View()
    model = Model()
    controller = Controller()

    view.iniciar()
    model.iniciar()
    controller.iniciar(view=view, model=model)

    view.mainloop()

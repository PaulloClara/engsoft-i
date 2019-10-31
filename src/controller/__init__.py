from src.controller.navbar import Navbar


class Controller:

    def __init__(self):
        self.__view = None
        self.__model = None

        self.navbar = Navbar(controller=self)

    def start(self, model, view):
        self.__view = view
        self.__model = model

        self.__view.start()

from src.controller.navbar import Navbar


class Controller:

    def __init__(self):
        self.view = None
        self.model = None

        self.navbar = Navbar(controller=self)

    def start(self, model, view):
        self.view = view
        self.model = model

        self.view.start()

from src.store import Store
from src.model.activity import Activity


class Model:

    def __init__(self, controller):
        self.__controller = controller

        self.store = Store()
        self.activity = Activity(controller=self.__controller, store=self.store)

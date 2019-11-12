from src.store import Store
from src.model.student import Student
from src.model.activity import Activity


class Model:

    def __init__(self, controller):
        self.__controller = controller

        self.store = Store()
        self.student = Student(model=self, controller=self.__controller)
        self.activity = Activity(controller=self.__controller, store=self.store)

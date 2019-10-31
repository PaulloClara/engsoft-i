class Controller:

    def __init__(self):
        self.__view = None
        self.__model = None

    def start(self, model, view):
        self.__view = view
        self.__model = model

        self.__view.start()

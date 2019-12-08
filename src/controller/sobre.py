class Sobre:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def evento_elemento_montado(self):
        self.view.sobre.iniciar()

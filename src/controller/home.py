class Home:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def carregar_cardes(self):
        pass

    def evento_click_no_label(self):
        pass

    def evento_elemento_montado(self):
        self.view.home.iniciar()

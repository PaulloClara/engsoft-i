from src.model.modelo import Modelo

class Sobre(Modelo):

    def __init__(self):
        super().__init__()

        self.tabela = 'sobre'
        self.cartoes = []

    def iniciar(self, model):
        self.model = model
        self.store = self.model.store

        self.obter_cartoes()

    def obter_cartoes(self):
        pass

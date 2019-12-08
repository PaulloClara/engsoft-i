class Sobre:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.sobre

        self.tabela = 'sobre'
        self.colunas = ['id_do_cartao', 'titulo', 'conteudo']

        self.cartoes = []

        self.obter_cartoes()

    def obter_cartoes(self):
        pass

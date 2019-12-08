class Home:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.home

        self.tabela = 'home'
        self.colunas = ['id_do_elemento', 'tipo', 'titulo', 'id_1', 'id_2']

        self.elementos = []

        self.obter_elementos()

    def obter_elementos(self):
        pass

class Home:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def carregar_apresentacoes(self):
        for apresentacao in self.model.apresentacao.apresentacoes:
            self.view.home.lista_de_elementos.adicionar(elemento=apresentacao)

    def evento_cadastrar_apresentacao(self):
        pass

    def evento_remover_apresentacao(self):
        pass

    def evento_ordenar_lista(self):
        pass

    def evento_click_no_label(self):
        pass

    def evento_elemento_montado(self):
        self.view.home.iniciar()
        self.carregar_apresentacoes()

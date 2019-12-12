class Home:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def carregar_apresentacoes(self):
        for apresentacao in self.model.apresentacao.apresentacoes:
            self.view.home.lista_de_elementos.adicionar(elemento=apresentacao)

    def evento_cadastrar_apresentacao(self):
        self.view.home.criar_janela_de_cadastro()

    def evento_confirmar_cadastro(self):
        pass
        # form = self.view.home.janela_de_cadastro.obter_campos()
        #
        # erro = self.model.apresentacao.validar_campos(formulario=form)
        # if erro:
        #     self.view.criar_janela_de_erro(erro=erro)
        #     return
        #
        # self.model.apresentacao.cadastrar_apresetacao(apresentacao=form)
        #
        # self.view.home.destruir_janela_de_cadastro()
        #
        # self.view.home.destruir_lista_de_elementos()
        # self.carregar_apresentacoes()

    def evento_cancelar_cadastro(self):
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

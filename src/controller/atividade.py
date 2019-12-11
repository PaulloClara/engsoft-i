class Atividade:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def carregar_atividades(self):
        for atv in self.model.atividade.atividades:
            self.view.atividade.lista_de_atividades.adicionar(atividade=atv)

    def evento_cadastrar(self):
        self.view.atividade.criar_janela_de_cadastro()

    def evento_remover_atividade(self, id_da_atividade):
        self.model.atividade.remover_atividade(id_da_atividade=id_da_atividade)

        self.view.atividade.destruir_lista_de_atividades()
        self.carregar_atividades()

    def evento_confirmar_cadastro(self):
        form = self.view.atividade.janela_de_cadastro.obter_campos()

        erro = self.model.atividade.validar_campos(formulario=form)
        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.model.atividade.cadastrar_atividade(atividade=form)
        self.view.atividade.destruir_janela_de_cadastro()

        self.view.atividade.destruir_lista_de_atividades()
        self.carregar_atividades()

    def evento_cancelar_cadastro(self):
        self.view.atividade.destruir_janela_de_cadastro()

    def evento_elemento_montado(self):
        self.view.atividade.iniciar()
        self.carregar_atividades()

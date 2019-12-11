class Grupo:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def carregar_grupos(self):
        for grupo in self.model.grupo.grupos:
            self.view.grupo.lista_de_grupos.adicionar(grupo=grupo)

    def evento_cadastrar(self):
        self.view.grupo.criar_janela_de_cadastro()

    def evento_cancelar_cadastro(self):
        self.view.grupo.destruir_janela_de_cadastro()

    def evento_remover_grupo(self, id_do_grupo):
        self.model.grupo.remover_grupo(id_do_grupo=id_do_grupo)

        self.view.grupo.destruir_lista_de_grupos()
        self.carregar_grupos()

    def evento_confirmar_cadastro(self):
        form = self.view.grupo.janela_de_cadastro.obter_campos()

        erro = self.model.grupo.validar_campos(formulario=form)
        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        grupos = self.model.grupo.gerar_grupos(formulario=form)

        for grupo in grupos:
            self.model.grupo.cadastrar_grupo(grupo=grupo)

        self.view.grupo.destruir_janela_de_cadastro()

        self.view.grupo.destruir_lista_de_grupos()
        self.carregar_grupos()

    def evento_elemento_montado(self):
        self.view.grupo.iniciar()
        self.carregar_grupos()

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
        formulario = self.view.grupo.janela_de_cadastro.obter_campos()

        estado_do_formulario = self.model.grupo.validar_campos(formulario=formulario)
        if estado_do_formulario != 'ok':
            self.view.grupo.criar_janela_de_erro(erro=estado_do_formulario)
            return

        grupos = self.model.grupo.gerar_grupos(formulario=formulario)

        for grupo in grupos:
            self.model.grupo.cadastrar_grupo(grupo=grupo)

        self.view.grupo.destruir_janela_de_cadastro()

        self.view.grupo.destruir_lista_de_grupos()
        self.carregar_grupos()

    def evento_elemento_montado(self):
        self.view.grupo.iniciar()
        self.carregar_grupos()

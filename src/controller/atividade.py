class Atividade:

    def __init__(self, controller):
        self.__controller = controller

    def carregar_atividades(self):
        view = self.__controller.view.atividade
        model = self.__controller.model.atividade

        for atividade in model.atividades:
            view.lista_de_atividades.adicionar(atividade=atividade)

    def evento_cadastrar(self):
        view = self.__controller.view.atividade

        if not view.janela_de_cadastro:
            view.criar_janela_de_cadastro()

    def evento_remover_atividade(self, id_da_atividade):
        view = self.__controller.view.atividade
        model = self.__controller.model.atividade

        model.remover_atividade(id_da_atividade=id_da_atividade)

        view.destruir_lista_de_atividades()
        self.carregar_atividades()

    def evento_confirmar_cadastro(self):
        view = self.__controller.view.atividade
        model = self.__controller.model.atividade

        formulario = view.janela_de_cadastro.obter_campos()

        estado_do_formulario = model.validar_campos(formulario=formulario)
        if estado_do_formulario != 'ok':
            self.__controller.view.criar_janela_de_erro(erro=estado_do_formulario)
            return

        model.cadastrar_atividade(atividade=formulario)
        view.destruir_janela_de_cadastro()

        view.destruir_lista_de_atividades()
        self.carregar_atividades()

    def evento_cancelar_cadastro(self):
        view = self.__controller.view.atividade
        view.destruir_janela_de_cadastro()

    def evento_montado(self):
        self.carregar_atividades()

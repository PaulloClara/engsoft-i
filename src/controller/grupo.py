class Grupo:

    def __init__(self, controller):
        self.__controller = controller

    def evento_cadastrar(self):
        view = self.__controller.view.grupo

        view.criar_janela_de_cadastro()

    def evento_cancelar_cadastro(self):
        view = self.__controller.view.grupo

        view.destruir_janela_de_cadastro()

    def evento_confirmar_cadastro(self):
        view = self.__controller.view.grupo
        model = self.__controller.model.grupo

        formulario = view.janela_de_cadastro.obter_campos()

        estado_do_formulario = model.validar_campos(formulario=formulario)
        if estado_do_formulario != 'ok':
            self.__controller.view.criar_janela_de_erro(erro=estado_do_formulario)
            return

        model.cadastrar_grupo(grupo=formulario)
        view.destruir_janela_de_cadastro()

    def evento_montado(self):
        pass

class Navbar:

    def __init__(self, controller):
        self.__controller = controller

    def evento_tela_de_aluno(self):
        if (self.__controller.view.container_ativo == 'aluno'):
            return

        self.__controller.view.destruir_container_ativo()
        self.__controller.view.criar_container_de_aluno()

    def evento_tela_de_atividade(self):
        if (self.__controller.view.container_ativo == 'atividade'):
            return

        self.__controller.view.destruir_container_ativo()
        self.__controller.view.criar_container_de_atividade()

    def evento_tela_de_grupo(self):
        if (self.__controller.view.container_ativo == 'grupo'):
            return

        self.__controller.view.destruir_container_ativo()
        self.__controller.view.criar_container_de_grupo()

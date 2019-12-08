class Navbar:

    def __init__(self, controller):
        self.view = controller.view

    def evento_tela_home(self):
        if (self.view.container_ativo == 'home'):
            return

        self.view.destruir_container_ativo()
        self.view.criar_container_home()

    def evento_tela_aluno(self):
        if (self.view.container_ativo == 'aluno'):
            return

        self.view.destruir_container_ativo()
        self.view.criar_container_aluno()

    def evento_tela_atividade(self):
        if (self.view.container_ativo == 'atividade'):
            return

        self.view.destruir_container_ativo()
        self.view.criar_container_atividade()

    def evento_tela_grupo(self):
        if (self.view.container_ativo == 'grupo'):
            return

        self.view.destruir_container_ativo()
        self.view.criar_container_grupo()

    def evento_tela_sobre(self):
        if (self.view.container_ativo == 'sobre'):
            return

        self.view.destruir_container_ativo()
        self.view.criar_container_sobre()

    def evento_elemento_montado(self):
        self.view.navbar.iniciar()

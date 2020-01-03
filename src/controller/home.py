class Home(object):

    def __init__(self):
        pass

    def iniciar(self, controller: object) -> None:
        self.view = controller.view
        self.model = controller.model

        self.cadastrar_tarefa = controller.tarefa.cadastrar
        self.cadastrar_apresentacao = controller.apresentacao.cadastrar

        self.configurar()

    def configurar(self) -> None:
        actions = self.view.home.actions.subelemento

        actions.tarefa.evento['<Button-1>'] = self.cadastrar_tarefa
        actions.cadastrar.evento['<Button-1>'] = self.cadastrar_apresentacao

        self.view.home.actions.carregar_eventos()

        self.view.home.cadastro_apresentacao.defs.mcnf['<Start>'] =\
            actions.cadastrar.desativar
        self.view.home.cadastro_apresentacao.defs.mcnf['<Destroy>'] =\
            actions.cadastrar.ativar

        self.view.home.cadastro_tarefa.defs.mcnf['<Start>'] =\
            actions.tarefa.desativar
        self.view.home.cadastro_tarefa.defs.mcnf['<Destroy>'] =\
            actions.tarefa.ativar

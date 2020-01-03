class Home(object):

    def __init__(self):
        pass

    def iniciar(self, controller: object):
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

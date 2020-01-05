class Home(object):

    def __init__(self):
        pass

    def iniciar(self, controller: object) -> None:
        self.view = controller.view
        self.model = controller.model

        self.cadastrar_tarefa = controller.tarefa.cadastrar
        self.cadastrar_apresentacao = controller.apresentacao.cadastrar

        self.configurar()

    def filtrar(self, evt, tipo: str) -> None:
        for elemento in self.view.home.listagem.elementos:
            if tipo != elemento.defs.tipo:
                elemento.ocultar()
                continue
            elemento.mostrar()

        self.view.home.filtro.desativar_(elemento=tipo)
        self.view.home.listagem.elemento_ativo = tipo

    def configurar(self) -> None:
        filtro = self.view.home.filtro.subelemento
        actions = self.view.home.actions.subelemento

        filtro.tarefa.evento['<Button-1>'] =\
            lambda evt: self.filtrar(evt, 'tarefa')
        filtro.apresentacao.evento['<Button-1>'] =\
            lambda evt: self.filtrar(evt, 'apresentacao')

        filtro.tarefa.desativar()

        actions.tarefa.evento['<Button-1>'] = self.cadastrar_tarefa
        actions.cadastrar.evento['<Button-1>'] = self.cadastrar_apresentacao

        self.view.home.filtro.carregar_eventos()
        self.view.home.actions.carregar_eventos()

        self.view.home.cadastro_apresentacao.defs.mcnf['<Start>'] =\
            actions.cadastrar.desativar
        self.view.home.cadastro_apresentacao.defs.mcnf['<Destroy>'] =\
            actions.cadastrar.ativar

        self.view.home.cadastro_tarefa.defs.mcnf['<Start>'] =\
            actions.tarefa.desativar
        self.view.home.cadastro_tarefa.defs.mcnf['<Destroy>'] =\
            actions.tarefa.ativar

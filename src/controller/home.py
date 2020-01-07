class Home(object):

    def __init__(self):
        pass

    def iniciar(self, controller: object) -> None:
        self.view = controller.view
        self.model = controller.model

        self.cadastrar_evento = controller.evento.cadastrar
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

        filtro.evento.evento['<Button-1>'] =\
            lambda evt: self.filtrar(evt, 'evento')
        filtro.tarefa.evento['<Button-1>'] =\
            lambda evt: self.filtrar(evt, 'tarefa')
        filtro.apresentacao.evento['<Button-1>'] =\
            lambda evt: self.filtrar(evt, 'apresentacao')

        filtro.tarefa.desativar()

        actions.evento.evento['<Button-1>'] = self.cadastrar_evento
        actions.tarefa.evento['<Button-1>'] = self.cadastrar_tarefa
        actions.apresentacao.evento['<Button-1>'] = self.cadastrar_apresentacao

        self.view.home.filtro.carregar_eventos()
        self.view.home.actions.carregar_eventos()

        self.view.home.cadastro_apresentacao.defs.mcnf['<Start>'] =\
            actions.apresentacao.desativar
        self.view.home.cadastro_apresentacao.defs.mcnf['<Destroy>'] =\
            actions.apresentacao.ativar

        self.view.home.cadastro_tarefa.defs.mcnf['<Start>'] =\
            actions.tarefa.desativar
        self.view.home.cadastro_tarefa.defs.mcnf['<Destroy>'] =\
            actions.tarefa.ativar

        self.view.home.cadastro_evento.defs.mcnf['<Start>'] =\
            actions.evento.desativar
        self.view.home.cadastro_evento.defs.mcnf['<Destroy>'] =\
            actions.evento.ativar

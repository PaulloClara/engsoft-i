class Actions(object):

    def __init__(self):
        pass

    def configurar(self) -> None:
        actions = self.view.atividade.actions.subelemento

        actions.cadastrar.evento['<Button-1>'] = self.cadastrar

        self.view.atividade.actions.carregar_eventos()

        self.view.atividade.cadastro.defs.mcnf['<Start>'] =\
            actions.cadastrar.desativar
        self.view.atividade.cadastro.defs.mcnf['<Destroy>'] =\
            actions.cadastrar.ativar

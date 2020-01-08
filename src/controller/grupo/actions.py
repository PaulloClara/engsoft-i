class Actions(object):

    def __init__(self):
        pass

    def configurar(self):
        actions = self.view.grupo.actions.subelemento

        actions.cadastrar.evento['<Button-1>'] = self.cadastrar

        self.view.grupo.actions.carregar_eventos()

        self.view.grupo.cadastro.defs.mcnf['<Start>'] =\
            actions.cadastrar.desativar
        self.view.grupo.cadastro.defs.mcnf['<Destroy>'] =\
            actions.cadastrar.ativar

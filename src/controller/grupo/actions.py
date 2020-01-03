class Actions(object):

    def __init__(self):
        pass

    def sortear(self, evt) -> None:
        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_apresentacao(evt=None)

    def configurar(self):
        actions = self.view.grupo.actions.subelemento

        actions.sortear.evento['<Button-1>'] = self.sortear
        actions.cadastrar.evento['<Button-1>'] = self.cadastrar

        self.view.grupo.actions.carregar_eventos()

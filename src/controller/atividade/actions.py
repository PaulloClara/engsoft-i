class Actions(object):

    def __init__(self):
        pass

    def sortear(self, evt):
        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_apresentacao(evt=None)

    def configurar(self) -> None:
        """Disparado quando o componente Atividade da View e montado."""
        actions = self.view.atividade.actions

        actions.subelemento.sortear.evento['<Button-1>'] = self.sortear
        actions.subelemento.cadastrar.evento['<Button-1>'] = self.cadastrar

        actions.carregar_eventos()

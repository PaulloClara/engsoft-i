class Actions(object):

    def __init__(self):
        pass

    def sortear(self, evt):
        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_tarefa(evt=None)

    def arquivo(self, evt) -> None:
        """Evento click do botao para carregar arquivo csv."""
        pass

    def configurar(self):
        actions = self.view.aluno.actions.subelemento

        actions.arquivo.evento['<Button-1>'] = self.arquivo
        actions.sortear.evento['<Button-1>'] = self.sortear

        self.view.aluno.actions.carregar_eventos()

"""Controller do Navbar."""


class Navbar(object):
    """Classe responsavle por gerenciar View e Model relacionados com Navbar."""

    def __init__(self) -> None:
        """Construtor padrao, define o atributo view."""
        pass

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model

        self.configurar()

    def tela_home(self, evt: object or None=None) -> None:
        """Evento click do botao home."""
        if self.view.container_ativo == 'home':
            return

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

    def tela_aluno(self, evt: object or None=None) -> None:
        """Evento click do botao aluno."""
        if self.view.container_ativo == 'aluno':
            return

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('aluno')

    def tela_atividade(self, evt: object or None=None) -> None:
        """Evento click do botao atividade."""
        if self.view.container_ativo == 'atividade':
            return

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('atividade')

    def tela_grupo(self, evt: object or None=None) -> None:
        """Evento click do botao grupo."""
        if self.view.container_ativo == 'grupo':
            return

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('grupo')

    def tela_sobre(self, evt: object or None=None) -> None:
        """Evento click do botao sobre."""
        if self.view.container_ativo == 'sobre':
            return

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('sobre')

    def configurar(self) -> None:
        navbar = self.view.navbar

        navbar.subelemento.home.evento['<Button-1>'] = self.tela_home
        navbar.subelemento.aluno.evento['<Button-1>'] = self.tela_aluno
        navbar.subelemento.grupo.evento['<Button-1>'] = self.tela_grupo
        navbar.subelemento.sobre.evento['<Button-1>'] = self.tela_sobre
        navbar.subelemento.atividade.evento['<Button-1>'] = self.tela_atividade

        navbar.carregar_eventos()

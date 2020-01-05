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

    def ativar_(self, evt, elemento: str):
        if self.view.container_ativo == elemento:
            return

        self.view.ocultar_container_ativo()
        self.view.mostrar_container(elemento)

    def configurar(self) -> None:
        navbar = self.view.navbar

        navbar.subelemento.home.evento['<Button-1>'] =\
            lambda evt: self.ativar_(evt, 'home')
        navbar.subelemento.aluno.evento['<Button-1>'] =\
            lambda evt: self.ativar_(evt, 'aluno')
        navbar.subelemento.grupo.evento['<Button-1>'] =\
            lambda evt: self.ativar_(evt, 'grupo')
        navbar.subelemento.sobre.evento['<Button-1>'] =\
            lambda evt: self.ativar_(evt, 'sobre')
        navbar.subelemento.atividade.evento['<Button-1>'] =\
            lambda evt: self.ativar_(evt, 'atividade')

        navbar.carregar_eventos()

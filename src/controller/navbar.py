"""Controller do Navbar."""


class Navbar(object):
    """Classe responsavle por gerenciar View e Model relacionados com Navbar.

    Attributes:
        view (View:obj): Objeto root View
    """

    def __init__(self, controller: object) -> None:
        """Construtor padrao, define o atributo view.

        Args:
            controller (Controller:obj): Objeto root Controller
        """
        self.view = controller.view

    def tela_home(self) -> None:
        """Evento click do botao home.

        - Verifica se o container Home ja esta ativo
            - sim -> para o evento
            - nao -> continua
        - Destroi container ativo
        - Cria container Home
        """
        if self.view.container_ativo == 'home':
            return

        self.view.desativar_container_ativo()

        self.view.home.ativar()
        self.view.container_ativo = 'home'

    def tela_aluno(self) -> None:
        """Evento click do botao aluno.

        - Verifica se o container Aluno ja esta ativo
            - sim -> para o evento
            - nao -> continua
        - Destroi container ativo
        - Cria container Aluno
        """
        if self.view.container_ativo == 'aluno':
            return

        self.view.desativar_container_ativo()

        self.view.aluno.ativar()
        self.view.container_ativo = 'aluno'

    def tela_atividade(self) -> None:
        """Evento click do botao atividade.

        - Verifica se o container Atividade ja esta ativo
            - sim -> para o evento
            - nao -> continua
        - Destroi container ativo
        - Cria container Atividade
        """
        if self.view.container_ativo == 'atividade':
            return

        self.view.desativar_container_ativo()

        self.view.atividade.ativar()
        self.view.container_ativo = 'atividade'

    def tela_grupo(self) -> None:
        """Evento click do botao grupo.

        - Verifica se o container Grupo ja esta ativo
            - sim -> para o evento
            - nao -> continua
        - Destroi container ativo
        - Cria container Grupo
        """
        if self.view.container_ativo == 'grupo':
            return

        self.view.desativar_container_ativo()

        self.view.grupo.ativar()
        self.view.container_ativo = 'grupo'

    def tela_sobre(self) -> None:
        """Evento click do botao sobre.

        - Verifica se o container Sobre ja esta ativo
            - sim -> para o evento
            - nao -> continua
        - Destroi container ativo
        - Cria container Sobre
        """
        if self.view.container_ativo == 'sobre':
            return

        self.view.desativar_container_ativo()

        self.view.sobre.ativar()
        self.view.container_ativo = 'sober'

    def elemento_montado(self) -> None:
        """Evento disparado quando o componente Navbar e montado.

        - Inicia o componente Navbar
        """
        self.view.navbar.iniciar()

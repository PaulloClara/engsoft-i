"""Controller da Home e da Apresentacao."""
from src.controller.home.eventos import Eventos


class Home(object):
    """Classe responsavel por gerenciar Home de View e Apresentacao de Model.

    Attributes:
        view (View:obj): Objeto root View
        model (Model:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Construtor padrao, define os atributos view e model."""
        self.view = controller.view
        self.model = controller.model

        self.eventos = Eventos(controller=self)

    def carregar_apresentacoes(self) -> None:
        """Carrega as apresentacoes na lista de eventos da Home na View."""
        for apresentacao in self.model.apresentacao.apresentacoes:
            self.view.home.lista.adicionar(apresentacao=apresentacao)

    def elemento_montado(self) -> None:
        """Disparado quando o componente Home na View e montado.

        - Inicia o container Home
        - Carrega a lista de apresentacoes
        """
        self.view.home.iniciar()
        self.carregar_apresentacoes()

        self.view.home.desativar()

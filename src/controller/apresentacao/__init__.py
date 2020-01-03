"""Controller da Home e da Apresentacao."""

from src.controller.apresentacao.listagem import Listagem
from src.controller.apresentacao.cadastro import Cadastro


class Apresentacao(Listagem, Cadastro):
    """Classe responsavel por gerenciar Home de View e Apresentacao de Model."""

    def __init__(self) -> None:
        """Construtor padrao, define os atributos view e model."""
        Listagem.__init__(self)
        Cadastro.__init__(self)

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model

        Listagem.configurar(self)

    def cadastrar(self, evt) -> None:
        """Evento click do botao cadastrar na actions."""
        self.view.home.cadastro_apresentacao.iniciar()
        Cadastro.configurar(self)

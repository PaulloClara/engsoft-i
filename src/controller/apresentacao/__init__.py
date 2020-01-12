from src.controller.apresentacao.listagem import Listagem
from src.controller.apresentacao.cadastro import Cadastro


class Apresentacao(Listagem, Cadastro):

    def __init__(self) -> None:
        Listagem.__init__(self)
        Cadastro.__init__(self)

    def iniciar(self, controller: object) -> None:
        self.view = controller.view
        self.model = controller.model

        Listagem.configurar(self)

    def cadastrar(self, evt) -> None:
        self.view.home.cadastro_apresentacao.iniciar()
        Cadastro.configurar(self)

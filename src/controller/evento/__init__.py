from src.controller.evento.listagem import Listagem
from src.controller.evento.cadastro import Cadastro


class Evento(Listagem, Cadastro):

    def __init__(self) -> None:
        Listagem.__init__(self)
        Cadastro.__init__(self)

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model

        Listagem.configurar(self)

    def cadastrar(self, evt) -> None:
        self.view.home.cadastro_evento.iniciar()
        Cadastro.configurar(self)

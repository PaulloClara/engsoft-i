from src.controller.tarefa.listagem import Listagem
from src.controller.tarefa.cadastro import Cadastro


class Tarefa(Listagem, Cadastro):

    def __init__(self) -> None:
        Listagem.__init__(self)
        Cadastro.__init__(self)

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model

        Listagem.configurar(self)

    def cadastrar(self, evt) -> None:
        self.view.home.cadastro_tarefa.iniciar()
        Cadastro.configurar(self)

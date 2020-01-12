from src.controller.atividade.actions import Actions
from src.controller.atividade.listagem import Listagem
from src.controller.atividade.cadastro import Cadastro


class Atividade(Actions, Listagem, Cadastro):

    def __init__(self) -> None:
        Actions.__init__(self)
        Listagem.__init__(self)
        Cadastro.__init__(self)

    def iniciar(self, controller: object):
        self.view = controller.view
        self.model = controller.model
        self.cadastrar_apresentacao = controller.apresentacao.cadastrar

        Actions.configurar(self)
        Listagem.configurar(self)

    def cadastrar(self, evt) -> None:
        self.view.atividade.cadastro.iniciar()
        Cadastro.configurar(self)

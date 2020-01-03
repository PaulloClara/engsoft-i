from src.utils.tk import TKUtils

from src.view.atividade.actions import Actions
from src.view.atividade.cadastro import Formulario
from src.view.atividade.listagem import ListaDeAtividades


class Atividade(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['side'] = 'bottom'

        self.actions = Actions()
        self.cadastro = Formulario()
        self.listagem = ListaDeAtividades()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.actions.iniciar(master=self)
        self.listagem.iniciar(master=self)

        self.ocultar()

from src.utils.tk import TKUtils

from src.view.grupo.actions import Actions
from src.view.grupo.cadastro import Formulario
from src.view.grupo.listagem import ListaDeGrupos


class Grupo(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['side'] = 'bottom'

        self.actions = Actions()
        self.cadastro = Formulario()
        self.listagem = ListaDeGrupos()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.actions.iniciar(master=self)
        self.listagem.iniciar(master=self)

        self.ocultar()

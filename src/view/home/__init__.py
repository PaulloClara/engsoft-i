from src.utils.tk import TKUtils

from src.view.home.filtro import Filtro
from src.view.home.actions import Actions
from src.view.home.listagem import ListaDeElementos
from src.view.home.cadastro import (FormularioApresentacao, FormularioTarefa,
                                    FormularioEvento)


class Home(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['side'] = 'bottom'

        self.filtro = Filtro()
        self.actions = Actions()
        self.listagem = ListaDeElementos()
        self.cadastro_evento = FormularioEvento()
        self.cadastro_tarefa = FormularioTarefa()
        self.cadastro_apresentacao = FormularioApresentacao()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.filtro.iniciar(master=self)
        self.actions.iniciar(master=self)
        self.listagem.iniciar(master=self)

        self.ocultar()

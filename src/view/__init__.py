from src import ICONE_MAIN
from src.utils.tk import TKUtils

from src.view.navbar import Navbar

from src.view.home import Home
from src.view.aluno import Aluno
from src.view.grupo import Grupo
from src.view.sobre import Sobre
from src.view.atividade import Atividade

from src.view.janela_erro import JanelaDeErro
from src.view.janela_sorteio import JanelaDeSorteio


class View(TKUtils.obter_janela()):

    def __init__(self):
        super().__init__()

        self.defs.cnf['icon'] = ICONE_MAIN
        self.defs.cnf['title'] = 'StuKi®'
        self.defs.cnf['geometry'] = '960x490'

        self.navbar = Navbar()

        self.home = Home()
        self.aluno = Aluno()
        self.grupo = Grupo()
        self.sobre = Sobre()
        self.atividade = Atividade()

        self.janela_erro = JanelaDeErro()
        self.janela_sorteio = JanelaDeSorteio()

        self.container_ativo = ''

    def iniciar(self):
        super().iniciar()

        self.navbar.iniciar(master=self)

        self.home.iniciar(master=self)
        self.aluno.iniciar(master=self)
        self.grupo.iniciar(master=self)
        self.sobre.iniciar(master=self)
        self.atividade.iniciar(master=self)

        self.mostrar_container('home')

    def mostrar_container(self, container):
        getattr(self, container).mostrar()

        self.navbar.desativar_(container)
        self.container_ativo = container

    def ocultar_container_ativo(self):
        getattr(self, self.container_ativo).ocultar()

        self.container_ativo = ''

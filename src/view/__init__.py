from src.utils.tk import TKUtils

from src.view.navbar import Navbar
from src.view.home import Home
from src.view.aluno import Aluno
from src.view.grupo import Grupo
from src.view.atividade import Atividade
from src.view.sobre import Sobre

from src.view.janela_de_erro import JanelaDeErro
from src.view.janela_de_sorteio import JanelaDeSorteio


class View(TKUtils.Janela()):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.navbar = None
        self.home = None
        self.aluno = None
        self.grupo = None
        self.atividade = None
        self.sobre = None

        self.janela_de_erro = None
        self.janela_de_sorteio = None

        self.container_ativo = ''

    def segundo_init(self):
        self.title('StuKi®')
        self.geometry('960x490')
        self.resizable(0, 0)

        TKUtils.definir_icone(master=self, nome_do_icone='icone')

    def iniciar(self):
        self.criar_navbar()

        self.criar_container_home()
        self.criar_container_aluno()
        self.criar_container_atividade()
        self.criar_container_grupo()
        self.criar_container_sobre()

        self.home.ativar()
        self.container_ativo = 'home'

        self.mainloop()

    def criar_navbar(self):
        controller = self.controller.navbar
        self.navbar = Navbar(master=self, controller=controller)

        self.controller.navbar.elemento_montado()

    def criar_container_home(self):
        controller = self.controller.home
        self.home = Home(master=self, controller=controller)

        self.controller.home.elemento_montado()

    def criar_container_aluno(self):
        controller = self.controller.aluno
        self.aluno = Aluno(master=self, controller=controller)

        self.controller.aluno.elemento_montado()

    def criar_container_atividade(self):
        controller = self.controller.atividade
        self.atividade = Atividade(master=self, controller=controller)

        self.controller.atividade.elemento_montado()

    def criar_container_grupo(self):
        controller = self.controller.grupo
        self.grupo = Grupo(master=self, controller=controller)

        self.controller.grupo.elemento_montado()

    def criar_container_sobre(self):
        controller = self.controller.sobre
        self.sobre = Sobre(master=self, controller=controller)

        self.controller.sobre.elemento_montado()

    def desativar_container_ativo(self):
        if self.container_ativo == 'home':
            self.home.desativar()
        elif self.container_ativo == 'aluno':
            self.aluno.desativar()
        elif self.container_ativo == 'atividade':
            self.atividade.desativar()
        elif self.container_ativo == 'grupo':
            self.grupo.desativar()
        elif self.container_ativo == 'sobre':
            self.sobre.desativar()

        self.container_ativo = ''

    def criar_janela_de_erro(self, erro):
        self.janela_de_erro = JanelaDeErro(erro=erro)

    def criar_janela_de_sorteio(self, atividade, aluno='', grupo=''):
        elemento = aluno if aluno else grupo['nome']

        self.janela_de_sorteio =\
            JanelaDeSorteio(elemento=elemento, atividade=atividade)

        self.janela_de_sorteio.iniciar()

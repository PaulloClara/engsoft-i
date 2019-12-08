from src.utils.tk import TKUtils

from src.view.navbar import Navbar
from src.view.aluno import Aluno
from src.view.grupo import Grupo
from src.view.atividade import Atividade

from src.view.janela_de_erro import JanelaDeErro
from src.view.janela_de_sorteio import JanelaDeSorteio


class View(TKUtils.Janela()):

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.navbar = None
        self.aluno = None
        self.grupo = None
        self.atividade = None

        self.janela_de_erro = None
        self.janela_de_sorteio = None

        self.container_ativo = ''

    def segundo_init(self):
        self.title('StuKi®')
        self.geometry('960x480')
        self.resizable(0, 0)

        TKUtils.definir_icone(master=self, nome_do_icone='icone')

    def iniciar(self):
        self.criar_navbar()
        self.criar_container_de_aluno()

        self.mainloop()

    def criar_navbar(self):
        eventos = {}
        eventos['aluno'] = self.controller.navbar.evento_tela_de_aluno
        eventos['grupo'] = self.controller.navbar.evento_tela_de_grupo
        eventos['atividade'] = self.controller.navbar.evento_tela_de_atividade

        self.navbar = Navbar(master=self, eventos=eventos)

    def criar_container_de_aluno(self):
        eventos = {}
        eventos['sortear'] = self.controller.sortear

        controller = self.controller.aluno
        self.aluno = Aluno(master=self, controller=controller, eventos=eventos)

        self.container_ativo = 'aluno'
        self.controller.aluno.evento_elemento_montado()

    def criar_container_de_atividade(self):
        eventos = {}
        eventos['sortear'] = self.controller.sortear

        controller = self.controller.atividade
        self.atividade =\
            Atividade(master=self, controller=controller, eventos=eventos)

        self.container_ativo = 'atividade'
        self.controller.atividade.evento_elemento_montado()

    def criar_container_de_grupo(self):
        eventos = {}
        eventos['sortear'] = self.controller.sortear

        controller = self.controller.grupo
        self.grupo = Grupo(master=self, controller=controller, eventos=eventos)

        self.container_ativo = 'grupo'
        self.controller.grupo.evento_elemento_montado()

    def destruir_container_ativo(self):
        if self.container_ativo == 'aluno':
            self.aluno.destroy()
        elif self.container_ativo == 'atividade':
            self.atividade.destroy()
        elif self.container_ativo == 'grupo':
            self.grupo.destroy()

        self.container_ativo = ''

    def criar_janela_de_erro(self, erro):
        self.janela_de_erro = JanelaDeErro(erro=erro)

    def criar_janela_de_sorteio(self, aluno, atividade):
        self.janela_de_sorteio = JanelaDeSorteio(aluno=aluno, atividade=atividade)

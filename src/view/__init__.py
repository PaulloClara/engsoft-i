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

        self.__controller = controller

        self.title('StuKi®')
        self.geometry('960x480')
        self.resizable(0, 0)

        TKUtils.definir_icone(master=self, nome_do_icone='icone')

        self.grupo = None
        self.navbar = None
        self.aluno = None
        self.atividade = None

        self.janela_de_erro = None
        self.janela_de_sorteio = None

        self.container_ativo = ''

    def iniciar(self):
        self.criar_navbar()
        self.criar_container_de_aluno()

        self.mainloop()

    def criar_navbar(self):
        eventos = {}

        eventos['aluno'] = self.__controller.navbar.evento_tela_de_aluno
        eventos['grupo'] = self.__controller.navbar.evento_tela_de_grupo
        eventos['atividade'] = self.__controller.navbar.evento_tela_de_atividade

        self.navbar = Navbar(master=self, eventos=eventos)

    def criar_container_de_aluno(self):
        eventos = {}

        eventos['sortear'] = self.__controller.sortear

        controller = self.__controller.aluno
        self.aluno = Aluno(master=self, controller=controller, eventos=eventos)

        self.container_ativo = 'aluno'

        self.__controller.aluno.evento_montado()

    def criar_container_de_atividade(self):
        eventos = {}

        eventos['sortear'] = self.__controller.sortear

        controller = self.__controller.atividade
        self.atividade =\
            Atividade(master=self, controller=controller, eventos=eventos)

        self.container_ativo = 'atividade'

        self.__controller.atividade.evento_montado()

    def criar_container_de_grupo(self):
        eventos = {}

        eventos['sortear'] = self.__controller.sortear

        controller = self.__controller.grupo
        self.grupo = Grupo(master=self, controller=controller, eventos=eventos)

        self.container_ativo = 'grupo'

        self.__controller.grupo.evento_montado()

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

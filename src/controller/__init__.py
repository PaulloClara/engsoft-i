"""Controller Root."""

from src.controller.navbar import Navbar

from src.controller.home import Home
from src.controller.aluno import Aluno
from src.controller.grupo import Grupo
from src.controller.sobre import Sobre
from src.controller.tarefa import Tarefa
from src.controller.atividade import Atividade
from src.controller.apresentacao import Apresentacao


class Controller(object):
    """Classe responsavel por gerenciar o fluxo de execucao da aplicacao."""

    def __init__(self) -> None:
        """Contrutor padrao, declara os atributos da classe."""
        self.view = None
        self.model = None

        self.navbar = Navbar()

        self.home = Home()
        self.aluno = Aluno()
        self.grupo = Grupo()
        self.sobre = Sobre()
        self.tarefa = Tarefa()
        self.atividade = Atividade()
        self.apresentacao = Apresentacao()

    def iniciar(self, view, model) -> None:
        """Instancia/cria os sub-objetos e inicializa Model root e View root."""
        self.view = view
        self.model = model

        self.navbar.iniciar(controller=self)

        self.home.iniciar(controller=self)
        self.aluno.iniciar(controller=self)
        self.grupo.iniciar(controller=self)
        self.sobre.iniciar(controller=self)
        self.tarefa.iniciar(controller=self)
        self.atividade.iniciar(controller=self)
        self.apresentacao.iniciar(controller=self)

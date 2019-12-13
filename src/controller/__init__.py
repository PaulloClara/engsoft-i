"""Controller Root."""

from src.controller.navbar import Navbar
from src.controller.home import Home
from src.controller.aluno import Aluno
from src.controller.grupo import Grupo
from src.controller.atividade import Atividade
from src.controller.sobre import Sobre


class Controller(object):
    """Classe responsavel por gerenciar o fluxo de execucao da aplicacao.

    Attributes:
        view (View:obj): Objeto root View.
        model (Model:obj): Objeto root Model.

        navbar (Controller:Navbar:obj): Padrao None.
        home (Controller:Home:obj): Padrao None.
        aluno (Controller:Aluno:obj): Padrao None.
        grupo (Controller:Grupo:obj): Padrao None.
        atividade (Controller:Atividade:obj): Padrao None.
        sobre (Controller:Sobre:obj): Padrao None.
    """

    def __init__(self) -> None:
        """Contrutor padrao, declara os atributos da classe."""
        self.view = None
        self.model = None

        self.navbar = None
        self.home = None
        self.aluno = None
        self.grupo = None
        self.atividade = None
        self.sobre = None

    def segundo_init(self, model: object, view: object) -> None:
        """Segundo contrutor, recebe os objetos Model e View instanciados.

        Args:
            model (Model:obj): Objeto root Model
            view (View:obj): Objeto root View
        """
        self.view = view
        self.model = model

    def iniciar(self) -> None:
        """Instancia/cria os sub-objetos e inicializa Model root e View root."""
        self.navbar = Navbar(controller=self)
        self.home = Home(controller=self)
        self.aluno = Aluno(controller=self)
        self.atividade = Atividade(controller=self)
        self.grupo = Grupo(controller=self)
        self.sobre = Sobre(controller=self)

        self.model.iniciar()
        self.view.iniciar()

"""Controller -> Nivel ROOT."""

from src.controller.navbar import Navbar
from src.controller.home import Home
from src.controller.aluno import Aluno
from src.controller.grupo import Grupo
from src.controller.atividade import Atividade
from src.controller.sobre import Sobre


class Controller:
    """Classe responsavel por gerenciar o fluxo de execucao da aplicacao.

    Attributes:
        view (View:obj): Padrao None.
        model (Model:obj): Padrao None.

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
        """Segundo contrutor, recebe os objetos Model e View instanciados."""
        self.view = view
        self.model = model

    def iniciar(self) -> None:
        """Inicializador, instancia/cria os sub-objetos."""
        self.navbar = Navbar(controller=self)
        self.home = Home(controller=self)
        self.aluno = Aluno(controller=self)
        self.atividade = Atividade(controller=self)
        self.grupo = Grupo(controller=self)
        self.sobre = Sobre(controller=self)

        self.model.iniciar()
        self.view.iniciar()

    def sortear(self, defs: dict) -> None:
        """Sorteador, realiza o sorteio de aluno/atividade."""
        erro, aluno, atividade = self.model.sortear(defs=defs)

        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.view.criar_janela_de_sorteio(aluno=aluno, atividade=atividade)

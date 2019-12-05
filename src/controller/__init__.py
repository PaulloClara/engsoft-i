from src.controller.navbar import Navbar
from src.controller.aluno import Aluno
from src.controller.atividade import Atividade
from src.controller.grupo import Grupo


class Controller:

    def __init__(self):
        self.view = None
        self.model = None

        self.navbar = None
        self.aluno = None
        self.atividade = None
        self.grupo = None

    def iniciar(self, model, view):
        self.view = view
        self.model = model

        self.navbar = Navbar(controller=self)
        self.aluno = Aluno(controller=self)
        self.atividade = Atividade(controller=self)
        self.grupo = Grupo(controller=self)

        self.view.iniciar()

    def sortear(self, defs={}):
        erro, aluno, atividade = self.model.sortear(defs=defs)

        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.view.criar_janela_de_sorteio(
            aluno=aluno, atividade=atividade['titulo'])

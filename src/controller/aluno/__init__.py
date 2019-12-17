"""Controller do Aluno."""
from src.controller.aluno.eventos import Eventos


class Aluno(object):
    """Classe responsavel por controlar componentes relacionados ao aluno.

    Attributes:
        view (View:obj): Objeto root View
        model (Model:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Construtor padrao, define define os atributos view e model.

        Args:
            controller (Controller:obj): Objeto root Controller
        """
        self.view = controller.view
        self.model = controller.model

        self.eventos = Eventos(controller=self)

    def carregar_lista_de_alunos(self) -> None:
        """Busca os alunos no model e cria os componentes visuais."""
        for aluno in self.model.aluno.alunos:
            self.view.aluno.lista.adicionar(nome_do_aluno=aluno)

    def elemento_montado(self) -> None:
        """Disparado quando o container Aluno for criado.

        - Inicia o componente Aluno
        - Carrega a lista de alunos na View
        """
        self.view.aluno.iniciar()
        self.carregar_lista_de_alunos()

        self.view.aluno.desativar()

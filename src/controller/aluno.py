"""Controller do Aluno."""


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

    def carregar_lista_de_alunos(self) -> None:
        """Busca os alunos no model e cria os componentes visuais."""
        for aluno in self.model.aluno.alunos:
            self.view.aluno.lista_de_alunos.adicionar(nome_do_aluno=aluno)

    def evento_carregar_arquivo(self) -> None:
        """Evento click do botao para carregar arquivo csv."""
        pass

    def evento_elemento_montado(self) -> None:
        """Evento disparado quando o container Aluno for criado.

        - Inicia o componente Aluno
        - Carrega a lista de alunos na View
        """
        self.view.aluno.iniciar()
        self.carregar_lista_de_alunos()

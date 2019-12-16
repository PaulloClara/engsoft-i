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

    def evento_sortear(self, valor=''):
        aluno = valor

        if not self.model.aluno.alunos:
            erro = 'Lista de alunos vazia'
            self.view.criar_janela_de_erro(erro=erro)
            return

        if not self.model.atividade.atividades:
            erro = 'Lista de atividades vazia'
            self.view.criar_janela_de_erro(erro=erro)
            return

        if not aluno:
            aluno = self.model.aluno.sortear()

        atividade = self.model.atividade.sortear()
        if not atividade:
            erro = 'Todas as atividades já estão em uso'
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.view.criar_janela_de_sorteio(atividade=atividade, aluno=aluno)

    def evento_carregar_arquivo(self) -> None:
        """Evento click do botao para carregar arquivo csv."""
        pass

    def evento_expandir_label(self, evento, elemento):
        pass

    def evento_elemento_montado(self) -> None:
        """Evento disparado quando o container Aluno for criado.

        - Inicia o componente Aluno
        - Carrega a lista de alunos na View
        """
        self.view.aluno.iniciar()
        self.carregar_lista_de_alunos()

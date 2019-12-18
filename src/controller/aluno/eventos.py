class Eventos(object):

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def sortear(self, valor=''):
        aluno = valor

        if not self.model.aluno.alunos:
            erro = 'Lista de Alunos vazia'
            self.view.criar_janela_de_erro(erro=erro)
            return

        if not self.model.atividade.atividades:
            erro = 'Lista de Atividades vazia'
            self.view.criar_janela_de_erro(erro=erro)
            return

        if not aluno:
            aluno = self.model.aluno.sortear()

        atividade = self.model.atividade.sortear()
        if not atividade:
            erro = 'Todas as Atividades já estão em uso'
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.view.criar_janela_de_sorteio(atividade=atividade, aluno=aluno)

    def carregar_arquivo(self) -> None:
        """Evento click do botao para carregar arquivo csv."""
        pass

    def expandir_label(self, evento, elemento):
        pass

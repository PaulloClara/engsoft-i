from src.view import View
from src.model import Model
from src.controller import Controller

from tests.exception import ExceptionNoTeste


class TesteDoModel:

    def __init__(self, loop):
        self.loop = loop

        controller = Controller()
        self.model = Model(controller=controller)
        view = View(controller=controller)
        controller.segundo_init(model=self.model, view=view)
        self.model.segundo_init()

    def iniciar(self):
        self.teste_do_init_do_aluno()
        self.teste_do_ler_arquivo_do_aluno()
        self.teste_do_limpar_linha_do_aluno()
        self.teste_geral_do_aluno()

    def teste_do_init_do_aluno(self):
        local = 'model.aluno.__init__'

        if self.model.aluno.alunos == []:
            erro = 'arquivo nao foi carregado'
            raise ExceptionNoTeste(local=local, erro=erro)

    def teste_do_ler_arquivo_do_aluno(self):
        local = 'model.aluno.ler_arquivo'

        self.model.aluno.alunos = []
        self.model.aluno.ler_arquivo()

        if self.model.aluno.alunos == []:
            erro = 'conteudo do arquivo nao foi carregado'
            raise ExceptionNoTeste(local=local, erro=erro)

    def teste_do_limpar_linha_do_aluno(self):
        pass

    def teste_geral_do_aluno(self):
        pass

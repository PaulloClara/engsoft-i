from src.utils import Utils
from src.utils.tk import TKUtils

from tests.exception import ExceptionNoTeste


class TesteDoUtils:

    def __init__(self, loop):
        self.loop = loop

        self.utils = Utils
        self.tk_utils = TKUtils

    def iniciar(self):
        self.teste_do_obter_inteiro_aleatorio()
        self.teste_do_caminho_de_execucao()

    def teste_do_obter_inteiro_aleatorio(self):
        local = 'utils.obter_inteiro_aleatorio'
        inteiro = self.utils.obter_inteiro_aleatorio(inicio=self.loop, fim=100)

        if not isinstance(inteiro, int):
            erro = 'nao retornou um inteiro'
            raise ExceptionNoTeste(local=local, erro=erro)

        if inteiro < self.loop or inteiro > 100:
            erro = 'nao respeitou o numero minimo e maximo'
            raise ExceptionNoTeste(local=local, erro=erro)

        if inteiro < 0:
            erro = 'inteiro negativo'
            raise ExceptionNoTeste(local=local, erro=erro)

    def teste_do_caminho_de_execucao(self):
        local = 'utils.obter_caminho_de_execucao'

        if self.utils.obter_caminho_de_execucao() != '':
            erro = 'valor precisa ser vazio'
            raise ExceptionNoTeste(local=local, erro=erro)

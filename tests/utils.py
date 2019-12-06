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

    def teste_do_obter_inteiro_aleatorio(self):
        local = 'utils.obter_inteiro_aleatorio'

        inteiro = self.utils.obter_inteiro_aleatorio(self.loop, 1000)

        if type(inteiro) != int:
            erro = 'nao retornou um inteiro'
            raise ExceptionNoTeste(local=local, erro=erro)
        if inteiro < self.loop or inteiro > 1000:
            erro = 'nao respeitou o numero minimo e maximo'
            raise ExceptionNoTeste(local=local, erro=erro)
        if inteiro < 0:
            erro = 'inteiro negativo'
            raise ExceptionNoTeste(local=local, erro=erro)

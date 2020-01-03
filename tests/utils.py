"""Conjunto de testes relacionados a todos os niveis de Utils."""

from src.utils import Utils
from src.utils.caminho import Caminho

from src.utils.tk import TKUtils

from tests.exception import ExceptionNoTeste


class TUtils(object):
    """Testes na camada root de Utils."""

    def __init__(self, loop) -> None:
        """Init padrao."""
        self.loop = loop

    def iniciar(self) -> None:
        """Segundo init."""
        self.inteiro_aleatorio()
        self.data_e_hora_atual()

        self.caminho_ate()

    def inteiro_aleatorio(self) -> None:
        """Testes de retorno."""
        local = 'utils.inteiro_aleatorio'

        erro = 'Nao retornou um inteiro'
        inteiro = Utils.inteiro_aleatorio(inicio=self.loop, fim=100)
        if not isinstance(inteiro, int):
            raise ExceptionNoTeste(local, erro)

        erro = 'Nao respeitou o numero minimo e maximo'
        inteiro = Utils.inteiro_aleatorio(inicio=self.loop, fim=100)
        if inteiro < self.loop or inteiro > 100:
            raise ExceptionNoTeste(local, erro)

        erro = 'Inteiro negativo'
        inteiro = Utils.inteiro_aleatorio(inicio=self.loop, fim=100)
        if inteiro < 0:
            raise ExceptionNoTeste(local, erro)

    def data_e_hora_atual(self) -> None:
        """Testes de retorno."""
        local = 'utils.data_e_hora_atual'

        erro = 'O valor nao e do tipo string'
        data_hora = Utils.data_e_hora_atual()
        if not isinstance(data_hora, str):
            raise ExceptionNoTeste(local, erro)

        erro = 'Formato invalido'
        data, hora = Utils.data_e_hora_atual().split(' ')
        if (len(data.split('/')) != 3 or len(data.replace('/', '')) != 8 or
            len(hora.split(':')) != 2 or len(hora.replace(':', '')) != 4):
            raise ExceptionNoTeste(local, erro)

    def caminho_ate(self) -> None:
        """Teste de retorno."""
        local = 'utils.caminho.ate'

        erro = 'O caminho nao esta completo'
        if Caminho.ate('caminho/do/arquivo.aqui')[0] != '/':
            raise ExceptionNoTeste(local, erro)

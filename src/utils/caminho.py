"""Submodulo de Utils."""

from os import getcwd
from src.utils.env import Env


class Caminho(object):
    """Conjunto caminhos relacionados a execucao e resolvedor de caminhos."""

    @staticmethod
    def ate(arquivo: str) -> str:
        """Resolve o caminho ate um arquivo de acordo com diversos fatores."""
        final = f'{Caminho.atual()}'
        if Env.modo_producao():
            final = f'{final}/lib'

        final = f'{final}/{arquivo}'

        return final

    @staticmethod
    def atual() -> str:
        """Caminho atual levando em conta o caminho do comando de execucao."""
        caminho = ''

        absoluto = getcwd()
        execucao = Caminho.execucao()

        if not execucao:
            caminho = absoluto
        elif execucao[0] != '/':
            caminho = f'{absoluto}/{execucao}'
        else:
            caminho = execucao

        return caminho

    @staticmethod
    def execucao() -> str:
        """Caminho em que o comando de execucao foi executado."""
        return '/'.join(Env.parametros()[0].split('/')[:-1])

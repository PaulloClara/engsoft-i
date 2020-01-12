from os import getcwd
from src.utils.env import Env


class Caminho(object):

    @staticmethod
    def ate(arquivo: str) -> str:
        final = f'{Caminho.atual()}'
        if Env.modo_producao():
            final = f'{final}/lib'

        final = f'{final}/{arquivo}'

        return final

    @staticmethod
    def atual() -> str:
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
        return '/'.join(Env.parametros()[0].split('/')[:-1])

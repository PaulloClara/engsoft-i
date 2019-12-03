from sys import argv
from os import getcwd
from random import randint


class Utils:

    @staticmethod
    def obter_inteiro_aleatorio(start, end):
        return randint(start, end)

    @staticmethod
    def obter_caminho_atual():
        caminho = getcwd()

        caminho_de_execucao = Utils.obter_caminho_de_execucao()
        if caminho_de_execucao != '':
            caminho = f'{caminho}/{caminho_de_execucao}'

        return caminho

    @staticmethod
    def obter_caminho(caminho_do_arquivo):
        caminho = Utils.obter_caminho_atual()

        if Utils.verificar_modo_producao():
            caminho = f'{caminho}/lib'

        caminho = f'{caminho}/{caminho_do_arquivo}'

        return caminho

    @staticmethod
    def obter_parametros():
        return argv

    @staticmethod
    def obter_caminho_de_execucao():
        return '/'.join(argv[0].split('/')[:-1])

    @staticmethod
    def verificar_modo_dev():
        if '--dev' in argv:
            return True
        return False

    @staticmethod
    def verificar_modo_teste():
        if '--test' in argv:
            return True
        return False

    @staticmethod
    def verificar_modo_producao():
        if not Utils.verificar_modo_dev() and not Utils.verificar_modo_teste():
            return True
        return False

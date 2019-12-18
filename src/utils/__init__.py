from sys import argv
from os import getcwd
from random import randint
from datetime import datetime


class Utils:

    @staticmethod
    def obter_inteiro_aleatorio(inicio, fim):
        return randint(inicio, fim)

    @staticmethod
    def obter_data_e_hora_atual():
        return datetime.now().strftime('%d/%m/%Y %H:%M')

    @staticmethod
    def obter_caminho_atual():
        caminho = ''
        caminho_absoluto = getcwd()
        caminho_de_execucao = Utils.obter_caminho_de_execucao()

        if caminho_de_execucao == '' or caminho_de_execucao[0] != '/':
            caminho = f'{caminho_absoluto}/{caminho_de_execucao}'
        else:
            caminho = caminho_de_execucao

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

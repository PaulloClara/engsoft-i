from tests.exception import ExceptionNoTeste

from tests.view import TesteDaView
from tests.model import TesteDoModel
from tests.utils import TUtils
from tests.store import TesteDoStore
from tests.controller import TesteDoController


class Tests(object):

    def __init__(self):
        self.qtd_testes = 10

    def iniciar(self):
        try:
            self.view()
            self.model()
            self.utils()
            self.store()
            self.controller()
        except Exception as erro:
            if not isinstance(erro, ExceptionNoTeste):
                print('\n\n\t Erro inesperado... \n\n')
                raise
            print(erro)

            exit(1)
        exit(0)

    def view(self):
        print('Testando View...', end='')

        for i in range(self.qtd_testes):
            TesteDaView(loop=i).iniciar()

        self.mostrar_ok(qtd_espacos=7)

    def model(self):
        print('Testando Model...', end='')

        for i in range(self.qtd_testes):
            TesteDoModel(loop=i).iniciar()

        self.mostrar_ok(qtd_espacos=6)

    def controller(self):
        print('Testando Controller...', end='')

        for i in range(self.qtd_testes):
            TesteDoController(loop=i).iniciar()

        self.mostrar_ok(qtd_espacos=1)

    def utils(self):
        print('Testando Utils...', end='')

        for i in range(self.qtd_testes):
            TUtils(loop=i).iniciar()

        self.mostrar_ok(qtd_espacos=6)

    def store(self):
        print('Testando Store...', end='')

        for i in range(self.qtd_testes):
            TesteDoStore(loop=i).iniciar()

        self.mostrar_ok(qtd_espacos=6)

    def mostrar_ok(self, qtd_espacos):
        print(f'\b\b\b{" " * qtd_espacos}->\033[1;32m OK', end='\033[0;0m\n')

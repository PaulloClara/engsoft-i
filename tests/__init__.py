from tests.exception import ExceptionNoTeste

from tests.view import TesteDaView
from tests.model import TesteDoModel
from tests.controller import TesteDoController
from tests.utils import TesteDoUtils
from tests.store import TesteDoStore


class Tests:

    def __init__(self):
        self.numero_de_testes = 10

    def iniciar(self):
        print('\n')

        try:
            print('Testando View...', end='')
            self.testar_view()

            print('Testando Model...', end='')
            self.testar_model()

            print('Testando Controller...', end='')
            self.testar_controller()

            print('Testando Utils...', end='')
            self.testar_utils()

            print('Testando Store...', end='')
            self.testar_store()
        except Exception as erro:
            if 'erro_msg' in dir(erro):
                self.mostrar_erro(erro_msg=erro)
            else:
                self.mostrar_erro(erro_msg='Erro inesperado...')
                raise

        print('\n')

    def testar_view(self):
        for i in range(self.numero_de_testes):
            TesteDaView(loop=i).iniciar()

        print('\b\b\b       ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_model(self):
        for i in range(self.numero_de_testes):
            TesteDoModel(loop=i).iniciar()

        print('\b\b\b      ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_controller(self):
        for i in range(self.numero_de_testes):
            TesteDoController(loop=i).iniciar()

        print('\b\b\b ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_utils(self):
        for i in range(self.numero_de_testes):
            TesteDoUtils(loop=i).iniciar()

        print('\b\b\b      ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_store(self):
        for i in range(self.numero_de_testes):
            TesteDoStore(loop=i).iniciar()

        print('\b\b\b      ->\033[1;32m OK', end='\033[0;0m\n')

    def mostrar_erro(self, erro_msg):
        print(f'\n\t\033[1;33m {erro_msg}', end='\033[0;0m\n')

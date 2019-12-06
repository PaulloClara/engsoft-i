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
            self.testar_view()
            self.testar_model()
            self.testar_controller()
            self.testar_utils()
            self.testar_store()
        except Exception as erro:
            self.mostrar_erro(erro_msg=erro)
            raise

        print('\n')

    def testar_view(self):
        print('Testando View...', end='')

        for i in range(self.numero_de_testes):
            TesteDaView(loop=i).iniciar()

        print('\b\b\b       ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_model(self):
        print('Testando Model...', end='')

        for i in range(self.numero_de_testes):
            TesteDoModel(loop=i).iniciar()

        print('\b\b\b      ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_controller(self):
        print('Testando Controller...', end='')

        for i in range(self.numero_de_testes):
            TesteDoController(loop=i).iniciar()

        print('\b\b\b ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_utils(self):
        print('Testando Utils...', end='')

        for i in range(self.numero_de_testes):
            TesteDoUtils(loop=i).iniciar()

        print('\b\b\b      ->\033[1;32m OK', end='\033[0;0m\n')

    def testar_store(self):
        print('Testando Store...', end='')

        for i in range(self.numero_de_testes):
            TesteDoStore(loop=i).iniciar()

        print('\b\b\b      ->\033[1;32m OK', end='\033[0;0m\n')

    def mostrar_erro(self, erro_msg):
        print(f'\n\t\033[1;33m {erro_msg}', end='\033[0;0m\n')

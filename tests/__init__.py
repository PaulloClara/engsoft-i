from tests.utils import TUtils
from tests.store import TStore

from tests.view import TView
from tests.model import TModel
from tests.controller import TController

from tests.exception import ExceptionNoTeste


class Tests(object):

    def __init__(self) -> None:
        self.qtd_testes = 10

    def iniciar(self) -> None:
        try:
            self.testar_('View')
            self.testar_('Model')
            self.testar_('Controller')

            self.testar_('Utils')
            self.testar_('Store')
        except Exception as erro:
            if not isinstance(erro, ExceptionNoTeste):
                raise
            print(erro)

            exit(1)
        exit(0)

    def testar_(self, componente: str) -> None:
        print(f'Testando {componente}...', end='')

        for i in range(self.qtd_testes):
            eval(f'T{componente}(loop=i).iniciar()')

        print(f'\b\b\b{" " * (11 - len(componente))}->\033[1;32m OK\033[0;0m')

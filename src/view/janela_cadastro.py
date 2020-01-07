"""."""

from src.utils.tk import TKUtils


class JanelaDeCadastro(TKUtils.obter_janela()):
    """."""

    def __init__(self, campos: int=2) -> None:
        """."""
        super().__init__()

        self.defs.qtd_campos = campos
        self.defs.cnf['geometry'] = f'420x{180 + campos * 30}'

        self.subelemento.main = TKUtils.obter_container(instanciar=True)
        self.subelemento.cancelar = TKUtils.obter_botao()
        self.subelemento.confirmar = TKUtils.obter_botao()

    def iniciar(self) -> None:
        """."""
        super().iniciar()

        self.criar_container_main()
        self.criar_botao_cancelar()
        self.criar_botao_confirmar()

    def criar_container_main(self) -> None:
        """."""
        self.subelemento.main.defs.cnf['bd'] = 10
        self.subelemento.main.defs.cnf['padx'] = 8

        self.subelemento.main.defs.grid['sticky'] = 'WE'

        self.subelemento.main.iniciar(master=self)

    def criar_botao_cancelar(self) -> None:
        """."""
        self.subelemento.cancelar.defs.cnf['text'] = 'Cancelar'
        self.subelemento.cancelar.defs.cnf['bg'] = 'red'

        self.subelemento.cancelar.defs.grid['row'] = self.defs.qtd_campos
        self.subelemento.cancelar.defs.grid['column'] = 0
        self.subelemento.cancelar.defs.grid['pady'] = 100
        self.subelemento.cancelar.defs.grid['sticky'] = 'W'

        self.subelemento.cancelar.iniciar(master=self.subelemento.main)

    def criar_botao_confirmar(self) -> None:
        """."""
        self.subelemento.confirmar.defs.cnf['text'] = 'Confirmar'
        self.subelemento.confirmar.defs.cnf['bg'] = 'green'

        self.subelemento.confirmar.defs.grid['row'] = self.defs.qtd_campos
        self.subelemento.confirmar.defs.grid['column'] = 1
        self.subelemento.confirmar.defs.grid['pady'] = 100
        self.subelemento.confirmar.defs.grid['sticky'] = 'E'

        self.subelemento.confirmar.iniciar(master=self.subelemento.main)

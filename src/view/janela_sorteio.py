"""."""

from src.utils.tk import TKUtils


class JanelaDeSorteio(TKUtils.obter_janela()):
    """."""

    def __init__(self) -> None:
        """."""
        super().__init__()

        self.defs.cnf['title'] = 'Grande Felizardo(a)'
        self.defs.cnf['geometry'] = f'600x180'

        self.subelemento.main = TKUtils.obter_container(instanciar=True)
        self.subelemento.sorteado = TKUtils.obter_label()
        self.subelemento.atividade = TKUtils.obter_label()
        self.subelemento.confirmar = TKUtils.obter_botao()
        self.subelemento.cancelar = TKUtils.obter_botao()

    def iniciar(self, atividade: str, evento, grupo='', aluno='') -> None:
        """."""
        super().iniciar()

        self.evento = evento
        self.sorteado = grupo if grupo else aluno
        self.atividade = atividade

        self.criar_container_main()
        self.criar_label_sorteado()
        self.criar_label_atividade()
        self.criar_botao_cancelar()
        self.criar_botao_confirmar()

    def criar_container_main(self) -> None:
        """."""
        self.subelemento.main.defs.cnf['bd'] = 10
        self.subelemento.main.iniciar(master=self)

    def criar_label_sorteado(self) -> None:
        """."""
        self.subelemento.sorteado.defs.cnf['text'] = self.sorteado
        self.subelemento.sorteado.defs.cnf['bd'] = 4
        self.subelemento.sorteado.defs.mcnf['fz'] = 22
        self.subelemento.sorteado.defs.cnf['fg'] =\
            'red' if 'Aluno' in self.sorteado else 'green'

        self.subelemento.sorteado.iniciar(master=self.subelemento.main)

    def criar_label_atividade(self) -> None:
        """."""
        self.subelemento.atividade.defs.cnf['text'] = self.atividade['titulo']
        self.subelemento.atividade.defs.cnf['bd'] = 4
        self.subelemento.atividade.defs.mcnf['fz'] = 22
        self.subelemento.atividade.defs.cnf['fg'] = 'blue'

        self.subelemento.atividade.iniciar(master=self.subelemento.main)

    def criar_botao_confirmar(self) -> None:
        """."""
        self.subelemento.confirmar.defs.cnf['text'] = 'Confirmar'
        self.subelemento.confirmar.defs.cnf['bg'] = 'green'
        self.subelemento.confirmar.defs.cnf['command'] = self.evento

        self.subelemento.confirmar.defs.pack['pady'] = 15
        self.subelemento.confirmar.defs.pack['side'] = 'right'

        self.subelemento.confirmar.iniciar(master=self.subelemento.main)

    def criar_botao_cancelar(self) -> None:
        """."""
        self.subelemento.cancelar.defs.cnf['text'] = 'Cancelar'
        self.subelemento.cancelar.defs.cnf['bg'] = 'red'
        self.subelemento.cancelar.defs.cnf['command'] = self.destroy

        self.subelemento.cancelar.defs.pack['pady'] = 15
        self.subelemento.cancelar.defs.pack['side'] = 'left'

        self.subelemento.cancelar.iniciar(master=self.subelemento.main)

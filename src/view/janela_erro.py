"""."""

from src.utils.tk import TKUtils


class JanelaDeErro(TKUtils.obter_janela()):
    """."""

    def __init__(self) -> None:
        """."""
        super().__init__()

        self.defs.cnf['title'] = 'Janela de Erro'
        self.defs.cnf['geometry'] = '340x200'

        self.subelemento.main = TKUtils.obter_container(instanciar=True)
        self.subelemento.mensagem = TKUtils.obter_mensagem()
        self.subelemento.confirmar = TKUtils.obter_botao()

    def iniciar(self, erro: str) -> None:
        """."""
        super().iniciar()

        self.msg_erro = erro

        self.inicializar_container_main()
        self.inicializar_mensagem_erro()
        self.inicializar_botao_confirmar()

    def inicializar_container_main(self) -> None:
        """."""
        self.subelemento.main.defs.cnf['bd'] = 10
        self.subelemento.main.defs.pack['expand'] = True

        self.subelemento.main.iniciar(master=self)

    def inicializar_mensagem_erro(self) -> None:
        """."""
        self.subelemento.mensagem.defs.cnf['text'] = self.msg_erro
        self.subelemento.mensagem.defs.cnf['fg'] = 'red'
        self.subelemento.mensagem.defs.cnf['width'] = 320
        self.subelemento.mensagem.defs.mcnf['fz'] = 20

        self.subelemento.mensagem.defs.pack['pady'] = 10

        self.subelemento.mensagem.iniciar(master=self.subelemento.main)

    def inicializar_botao_confirmar(self) -> None:
        """."""
        self.subelemento.confirmar.defs.cnf['text'] = 'OK'
        self.subelemento.confirmar.defs.cnf['bg'] = 'green'
        self.subelemento.confirmar.defs.cnf['command'] = self.destroy

        self.subelemento.confirmar.defs.pack['pady'] = 25
        self.subelemento.confirmar.defs.pack['side'] = 'bottom'

        self.subelemento.confirmar.iniciar(master=self.subelemento.main)

"""Intermediador entre o Tkinter e a camada View do App."""

from src.utils.tk.botao import MBotao
from src.utils.tk.label import MLabel
from src.utils.tk.input import MInput
from src.utils.tk.janela import MJanela
from src.utils.tk.mensagem import MMensagem
from src.utils.tk.container import MContainer
from src.utils.tk.scrollview import MScrollView


class TKUtils(object):
    """Serve instancias customizadas de classes TK."""

    @staticmethod
    def obter_label() -> MLabel:
        """Devolve uma instancia de MLabel."""
        return MLabel()

    @staticmethod
    def obter_mensagem() -> MMensagem:
        """Devolve uma instancia de MMensagem."""
        return MMensagem()

    @staticmethod
    def obter_botao() -> MBotao:
        """Devolve uma instancia de MBotao."""
        return MBotao()

    @staticmethod
    def obter_input() -> MInput:
        """Devolve uma instancia de MInput."""
        return MInput()

    @staticmethod
    def obter_container(instanciar: bool=False) -> MContainer:
        """Devolve uma instancia de MContainer."""
        return MContainer() if instanciar else MContainer

    @staticmethod
    def obter_scrollview(instanciar: bool=False) -> MScrollView:
        """Devolve uma instancia de MScrollView."""
        return MScrollView() if instanciar else MScrollView

    @staticmethod
    def obter_janela(instanciar: bool=False) -> MJanela:
        """Devolve uma instancia de MJanela."""
        return MJanela() if instanciar else MJanela

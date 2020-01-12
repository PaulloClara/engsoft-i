from src.utils.tk.botao import MBotao
from src.utils.tk.label import MLabel
from src.utils.tk.input import MInput
from src.utils.tk.janela import MJanela
from src.utils.tk.mensagem import MMensagem
from src.utils.tk.container import MContainer
from src.utils.tk.scrollview import MScrollView


class TKUtils(object):

    @staticmethod
    def obter_label() -> MLabel:
        return MLabel()

    @staticmethod
    def obter_mensagem() -> MMensagem:
        return MMensagem()

    @staticmethod
    def obter_botao() -> MBotao:
        return MBotao()

    @staticmethod
    def obter_input() -> MInput:
        return MInput()

    @staticmethod
    def obter_container(instanciar: bool=False) -> MContainer:
        return MContainer() if instanciar else MContainer

    @staticmethod
    def obter_scrollview(instanciar: bool=False) -> MScrollView:
        return MScrollView() if instanciar else MScrollView

    @staticmethod
    def obter_janela(instanciar: bool=False) -> MJanela:
        return MJanela() if instanciar else MJanela

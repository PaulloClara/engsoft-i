from src.utils.tk import TKUtils


class Sobre(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['side'] = 'bottom'

    def iniciar(self, master):
        super().iniciar(master=master)

        self.ocultar()

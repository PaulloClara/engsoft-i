from src.utils.tk import TKUtils


class Home(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def iniciar(self):
        self.pack(side='bottom')

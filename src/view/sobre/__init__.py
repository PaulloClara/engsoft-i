from src.utils.tk import TKUtils


class Sobre(TKUtils.Container()):

    def __init__(self, master):
        super().__init__(master=master)

    def iniciar(self):
        self.pack(side='bottom')

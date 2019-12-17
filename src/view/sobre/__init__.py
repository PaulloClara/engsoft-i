from src.utils.tk import TKUtils


class Sobre(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

    def iniciar(self):
        self.pack(side='bottom')

    def ativar(self):
        self.pack_configure(side='bottom')

    def desativar(self):
        self.pack_forget()

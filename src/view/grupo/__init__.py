from src.utils.tk import TKUtils


class Grupo(TKUtils.Container()):

    def __init__(self, master):
        super().__init__(master=master)
        self.pack()

        label = TKUtils.obter_label(master=self, cnf={'text': 'Grupos'})

from tkinter import Frame
from src.utils.tk.elemento import Elemento


class MContainer(Frame, Elemento):

    def __init__(self) -> None:
        Elemento.__init__(self)

        self.defs.cnf['bd'] = 2

    def iniciar(self, master: object) -> None:
        Frame.__init__(self, master=master, cnf=self.defs.cnf)
        self.mostrar()

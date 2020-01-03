"""Frame de TK personalizado."""

from tkinter import Frame
from src.utils.tk.elemento import Elemento


class MContainer(Frame, Elemento):
    """Estende a classe Frame de TK abstraindo algumas configuracoes."""

    def __init__(self) -> None:
        """Define as configuracoes padroes."""
        Elemento.__init__(self)

        self.defs.cnf['bd'] = 2

    def iniciar(self, master: object) -> None:
        """Inicializa e configura."""
        Frame.__init__(self, master=master, cnf=self.defs.cnf)
        self.mostrar()

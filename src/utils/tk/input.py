"""Entry de TK personalizado."""

from tkinter import Entry
from src.utils.tk.elemento import Elemento


class MInput(Entry, Elemento):
    """Estende a classe Entry de TK abstraindo algumas configuracoes."""

    def __init__(self) -> None:
        """Define as configuracoes padroes."""
        Elemento.__init__(self)

        self.defs.cnf['bd'] = 0
        self.defs.cnf['width'] = 20
        self.defs.cnf['bg'] = 'white'
        self.defs.cnf['fg'] = 'black'
        self.defs.cnf['justify'] = 'left'
        self.defs.cnf['font'] = ('times new roman', 14, 'italic')

        self.defs.mcnf['focus'] = False
        self.defs.mcnf['placeholder'] = 'Digite algo...'

    def iniciar(self, master: object) -> None:
        """Inicializa e configura."""
        Entry.__init__(self, master=master, cnf=self.defs.cnf)

        self.insert(0, self.defs.mcnf['placeholder'])
        if self.defs.mcnf['focus']:
            self.focus()

        self.mostrar()

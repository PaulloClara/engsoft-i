"""Tk de TK personalizado."""

from tkinter import Tk, PhotoImage
from src.utils.tk.elemento import Elemento


class MJanela(Tk, Elemento):
    """Estende a classe Tk de TK abstraindo algumas configuracoes."""

    def __init__(self) -> None:
        """Define as configuracoes padroes."""
        Elemento.__init__(self)

        self.defs.cnf['title'] = 'JANELA SEM TITULO'
        self.defs.cnf['geometry'] = '400x400'
        self.defs.cnf['resizable'] = False

    def iniciar(self) -> None:
        """Inicializa e configura."""
        Tk.__init__(self)

        if 'icon' in self.defs.cnf:
            self.wm_iconphoto(True, PhotoImage(file=self.defs.cnf['icon']))

        self.title(self.defs.cnf['title'])
        self.geometry(self.defs.cnf['geometry'])

        if not self.defs.cnf['resizable']:
            self.resizable(0, 0)

    def fechar(self) -> None:
        """Destroi a janela"""
        self.destroy()

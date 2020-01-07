"""Tk de TK personalizado."""

from tkinter import Tk, PhotoImage
from src.utils.tk.elemento import Elemento
from src.utils.tk.container import MContainer


class MJanela(Tk, Elemento):
    """Estende a classe Tk de TK abstraindo algumas configuracoes."""

    def __init__(self) -> None:
        """Define as configuracoes padroes."""
        Elemento.__init__(self)

        self.defs.cnf['title'] = 'JANELA SEM TITULO'
        self.defs.cnf['geometry'] = '400x400'
        self.defs.cnf['resizable'] = False

        self.subelemento.main = MContainer()
        self.subelemento.main.defs.cnf['bd'] = 10
        self.subelemento.main.defs.cnf['padx'] = 8

        self.ativa = False

    def iniciar(self) -> None:
        """Inicializa e configura."""
        Tk.__init__(self)
        self.subelemento.main.iniciar(master=self)

        self.protocol('WM_DELETE_WINDOW', self.fechar)

        if 'icon' in self.defs.cnf:
            self.wm_iconphoto(True, PhotoImage(file=self.defs.cnf['icon']))

        self.title(self.defs.cnf['title'])
        self.geometry(self.defs.cnf['geometry'])

        if not self.defs.cnf['resizable']:
            self.resizable(0, 0)

        if '<Start>' in self.defs.mcnf:
            self.defs.mcnf['<Start>']()

        self.ativa = True

    def fechar(self) -> None:
        """Destroi a janela"""
        if '<Destroy>' in self.defs.mcnf:
            self.defs.mcnf['<Destroy>']()

        self.destroy()
        self.ativa = False

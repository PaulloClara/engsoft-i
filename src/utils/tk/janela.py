from tkinter import Tk, PhotoImage
from src.utils.tk.elemento import Elemento
from src.utils.tk.container import MContainer


class MJanela(Tk, Elemento):

    def __init__(self) -> None:
        Elemento.__init__(self)

        self.defs.cnf['title'] = 'JANELA SEM TITULO'
        self.defs.cnf['geometry'] = '400x400'
        self.defs.cnf['resizable'] = False

        self.subelemento.main = MContainer()
        self.subelemento.main.defs.cnf['bd'] = 10
        self.subelemento.main.defs.cnf['padx'] = 8

        self.ativa = False

    def iniciar(self) -> None:
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
        if not self.ativa:
            return

        if '<Destroy>' in self.defs.mcnf:
            self.defs.mcnf['<Destroy>']()

        self.destroy()
        self.ativa = False

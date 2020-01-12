from tkinter import Button
from src.utils.tk.elemento import Elemento


class MBotao(Button, Elemento):

    def __init__(self) -> None:
        Elemento.__init__(self)

        self.defs.cnf['text'] = 'BOTAO'
        self.defs.cnf['width'] = 10
        self.defs.cnf['height'] = 1
        self.defs.cnf['bd'] = 2
        self.defs.cnf['pady'] = 6
        self.defs.cnf['padx'] = 6
        self.defs.cnf['bg'] = 'grey'
        self.defs.cnf['fg'] = 'white'
        self.defs.cnf['relief'] = 'solid'
        self.defs.cnf['font'] = ('times new roman', 14, 'bold')

        self.ativo = True

    def iniciar(self, master: object) -> None:
        if 'fz' in self.defs.mcnf:
            fonte = self.defs.cnf['font']
            self.defs.cnf['font'] = (fonte[0], self.defs.mcnf['fz'], fonte[2])

        Button.__init__(self, master=master, cnf=self.defs.cnf)
        self.mostrar()

    def ativar(self) -> None:
        self.configure(state='normal', bg=self.defs.cnf['bg'])
        self.ativo = True

        self.carregar_eventos()

    def desativar(self) -> None:
        self.configure(state='disabled', bg='grey', command=None)

        for key in self.evento:
            self.unbind(key)

        self.ativo = False

    def carregar_eventos(self) -> None:
        if not self.ativo:
            return

        if 'command' in self.defs.mcnf:
            self.configure(command=self.defs.mcnf['command'])

        Elemento.carregar_eventos(self)

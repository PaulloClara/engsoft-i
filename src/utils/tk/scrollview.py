from tkinter import Frame, Canvas, Scrollbar
from src.utils.tk.elemento import Elemento


class MScrollView(Frame, Elemento):
    """Conjunto de classes TK para listagem de elementos.

    obs: canvas, viewport e scrollbar nao sao subelementos pq o objetivo e criar
         um novo tipo de objeto que ate entao nao existe por padrao no TK.
    """

    def __init__(self) -> None:
        Elemento.__init__(self)

        self.defs.pack['expand'] = True

        self.defs.canvas = {}
        self.defs.viewport = {}
        self.defs.scrollbar = {}

    def iniciar(self, master: object) -> None:
        Frame.__init__(self, master=master, cnf=self.defs.cnf)

        self.canvas = Canvas(master=self, cnf=self.defs.canvas)
        self.viewport = Frame(master=self.canvas, cnf=self.defs.viewport)
        self.scrollbar = Scrollbar(master=self, cnf=self.defs.scrollbar)

        self.scrollbar.configure(command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        jnl, ar, tags = self.viewport, 'nw', 'self.viewport'
        self.canvas_window =\
            self.canvas.create_window((4, 4), window=jnl, anchor=ar, tags=tags)

        self.canvas.bind('<Configure>', self.evento_configurar_canvas)
        self.viewport.bind('<Configure>', self.evento_configurar_viewport)

        self.evento_configurar_viewport(None)

        self.mostrar()

    def evento_configurar_viewport(self, evt) -> None:
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def evento_configurar_canvas(self, evt) -> None:
        self.canvas.itemconfig(self.canvas_window, width=evt.width)

import tkinter as tk
from src.utils import Utils


class TKUtils:

    @staticmethod
    def definir_icone(master, nome_do_icone):
        arquivo = Utils.obter_caminho(f'src/assets/{nome_do_icone}.png')
        imagem = tk.PhotoImage(file=arquivo)
        master.wm_iconphoto(True, imagem)

    @staticmethod
    def obter_label(master, cnf={}, pack={}, grid={}):
        cnf_padrao = {}

        cnf_padrao['text'] = '...'
        cnf_padrao['font'] = ('times new roman', 14, 'bold')

        label = tk.Label(master=master, cnf=cnf_padrao)
        label.configure(cnf=cnf)

        if grid:
            label.grid(grid)
        else:
            label.pack(pack)

        label.style_cnf = cnf
        label.default_style_cnf = cnf_padrao

        return label

    @staticmethod
    def obter_botao(master, cnf={}, pack={}, grid={}):
        cnf_padrao = {}

        cnf_padrao['text'] = '...'
        cnf_padrao['width'] = 10
        cnf_padrao['height'] = 1
        cnf_padrao['bd'] = 2
        cnf_padrao['pady'] = 6
        cnf_padrao['padx'] = 6
        cnf_padrao['fg'] = 'white'
        cnf_padrao['font'] = ('times new roman', 14, 'bold')

        botao = tk.Button(master=master, cnf=cnf_padrao)
        botao.configure(cnf=cnf)

        if grid:
            botao.grid(grid)
        else:
            botao.pack(pack)

        botao.style_cnf = cnf
        botao.default_style_cnf = cnf_padrao

        return botao

    @staticmethod
    def obter_input(master, cnf={}, pack={}, grid={}):
        cnf_padrao = {}

        cnf_padrao['width'] = 20
        cnf_padrao['bg'] = 'white'
        cnf_padrao['fg'] = 'black'
        cnf_padrao['bd'] = 0
        cnf_padrao['justify'] = 'left'
        cnf_padrao['font'] = ('times new roman', 14, 'italic')

        _input = tk.Entry(master=master, cnf=cnf_padrao)

        if 'placeholder' in cnf:
            _input.insert(0, cnf['placeholder'])
            cnf.pop('placeholder')

        _input.configure(cnf=cnf)

        if grid:
            _input.grid(grid)
        else:
            _input.pack(pack)

        _input.style_cnf = cnf
        _input.default_style_cnf = cnf_padrao

        return _input

    @staticmethod
    def obter_container(master, cnf={}, pack={}, grid={}):
        container = tk.Frame(master=master, cnf=cnf)

        if grid:
            container.grid(grid)
        else:
            container.pack(pack)

        container.style_cnf = cnf

        return container

    @staticmethod
    def obter_janela(titulo='Nova Janela', tamanho='200x100'):
        janela = tk.Tk()

        janela.title(titulo)
        janela.geometry(tamanho)

        janela.style_cnf = cnf
        janela.default_style_cnf = cnf_padrao

        return janela

    @staticmethod
    def Janela():
        return tk.Tk

    @staticmethod
    def Container():
        return tk.Frame

    @staticmethod
    def ScrollContainer():
        return ScrollContainer


class ScrollContainer(tk.Frame):

    def __init__(self, master, cnf={}, cs_cnf={}, vt_cnf={}, sr_cnf={}):
        super().__init__(master=master, cnf=cnf)
        self.pack(expand=True)

        self.canvas = tk.Canvas(master=self, cnf=cs_cnf)
        self.viewport = tk.Frame(master=self.canvas, cnf=vt_cnf)
        self.scrollbar = tk.Scrollbar(
            master=self, cnf=sr_cnf, command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)
        self.canvas_window =\
            self.canvas.create_window(
                (4, 4), window=self.viewport, anchor='nw', tags='self.viewport')

        self.viewport.bind('<Configure>', self.on_frame_configure)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.on_frame_configure(None)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

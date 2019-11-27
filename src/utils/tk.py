import tkinter as tk
from src.utils import Utils


class TKUtils:

    @staticmethod
    def get_label(master, cnf={}, pack={}, grid={}):
        default_cnf = {}

        default_cnf['text'] = '...'
        default_cnf['font'] = ('arial', 12, 'bold')

        label = tk.Label(master=master, cnf=default_cnf)
        label.configure(cnf=cnf)

        if grid:
            label.grid(grid)
        else:
            label.pack(pack)

        return label

    @staticmethod
    def get_button(master, cnf={}, pack={}, grid={}):
        default_cnf = {}

        default_cnf['text'] = '...'
        default_cnf['width'] = 10
        default_cnf['height'] = 1
        default_cnf['bd'] = 2
        default_cnf['pady'] = 6
        default_cnf['padx'] = 6
        default_cnf['fg'] = 'white'
        default_cnf['font'] = ('arial', 12, 'bold')

        button = tk.Button(master=master, cnf=default_cnf)
        button.configure(cnf=cnf)

        if grid:
            button.grid(grid)
        else:
            button.pack(pack)

        return button

    @staticmethod
    def get_input(master, cnf={}, pack={}, grid={}):
        default_cnf = {}

        default_cnf['width'] = 20
        default_cnf['bg'] = 'white'
        default_cnf['fg'] = 'black'
        default_cnf['bd'] = 0
        default_cnf['justify'] = 'left'
        default_cnf['font'] = ('arial', 12, 'italic')

        _input = tk.Entry(master=master, cnf=default_cnf)
        _input.configure(cnf=cnf)

        if grid:
            _input.grid(grid)
        else:
            _input.pack(pack)

        return _input

    @staticmethod
    def get_container(master, cnf={}, pack={}, grid={}):
        container = tk.Frame(master=master, cnf=cnf)

        if grid:
            container.grid(grid)
        else:
            container.pack(pack)

        return container

    @staticmethod
    def get_window(title='New Window', size='200x100'):
        window = tk.Tk()

        window.title(title)
        window.geometry(size)

        return window

    @staticmethod
    def Window():
        return tk.Tk

    @staticmethod
    def Container():
        return tk.Frame

    @staticmethod
    def ScrollContainer():
        return ScrollContainer

    @staticmethod
    def set_icon(master, icon_name):
        file = Utils.get_full_path(f'src/assets/{icon_name}.png')
        image = tk.PhotoImage(file=file)
        master.wm_iconphoto(True, image)


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

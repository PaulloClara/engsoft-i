import tkinter as tk


class TKUtils:

    def __init__(self):
        self.Window = tk.Tk
        self.Container = tk.Frame
        self.ScrollFrame = ScrollFrame

        self.__label_config = {}
        self.__label_config['text'] = '...'
        self.__label_config['font'] = ('arial', 12, 'bold')

        self.__button_config = {}
        self.__button_config['text'] = '...'
        self.__button_config['width'] = 10
        self.__button_config['height'] = 1
        self.__button_config['bd'] = 3
        self.__button_config['pady'] = 6
        self.__button_config['padx'] = 6
        self.__button_config['font'] = ('arial', 14, 'bold')

        self.__entry_config = {}
        self.__entry_config['width'] = 20
        self.__entry_config['bg'] = "white"
        self.__entry_config['fg'] = "black"
        self.__entry_config['bd'] = 0
        self.__entry_config['justify'] = 'left'
        self.__entry_config['font'] = ('arial', 13, 'italic')

    def get_label(self, master, cnf={}, pack={}, grid={}):
        label = tk.Label(master=master, cnf=self.__label_config)
        label.configure(cnf=cnf)

        if grid:
            label.grid(grid)
        else:
            label.pack(pack)

        return label

    def get_button(self, master, cnf={}, pack={}, grid={}):
        button = tk.Button(master=master, cnf=self.__button_config)
        button.configure(cnf=cnf)

        if grid:
            button.grid(grid)
        else:
            button.pack(pack)

        return button

    def get_input(self, master, cnf={}, pack={}, grid={}):
        _input = tk.Entry(master=master, cnf=self.__entry_config)
        _input.configure(cnf=cnf)

        if grid:
            _input.grid(grid)
        else:
            _input.pack(pack)

        return _input

    def get_container(self, master, cnf={}, pack={}, grid={}):
        container = self.Container(master=master, cnf=cnf)

        if grid:
            container.grid(grid)
        else:
            container.pack(pack)

        return container

    def get_window(self, title='New Window', size='200x100'):
        window = self.Window()

        window.title(title)
        window.geometry(size)

        return window


class ScrollFrame(tk.Frame):

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


UI = TKUtils()

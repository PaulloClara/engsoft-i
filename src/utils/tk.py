from tkinter import *


class GUI:
    
    def __init__(self):
        self.Window = Tk
        self.Container = Frame
        self.Input = Entry
        self.Button = Button
        self.Label = Label

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

        self.__input_config = {}
        self.__input_config['width'] = 20
        self.__input_config['bg'] = "white"
        self.__input_config['fg'] = "black"
        self.__input_config['bd'] = 0
        self.__input_config['justify'] = 'left'
        self.__input_config['font'] = ('arial', 13, 'italic')

    def get_label(self, master, cnf={}, pack={}, grid={}):
        label = self.Label(master=master, cnf=self.__label_config)
        label.configure(cnf=cnf)

        if grid:
            label.grid(grid)
        else:
            label.pack(pack)

        return label

    def get_button(self, master, cnf={}, pack={}, grid={}):
        button = self.Button(master=master, cnf=self.__button_config)
        button.configure(cnf=cnf)

        if grid:
            button.grid(grid)
        else:
            button.pack(pack)

        return button

    def get_input(self, master, cnf={}, pack={}, grid={}):
        _input = self.Input(master=master, cnf=self.__input_config)
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


UI = GUI()

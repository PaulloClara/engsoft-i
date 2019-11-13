from src.utils.tk import UI


class Group(UI.Container):

    def __init__(self, master):
        super().__init__(master=master)
        self.pack()

        label_temp = UI.get_label(master=self, cnf={'text': 'Grupos'})
